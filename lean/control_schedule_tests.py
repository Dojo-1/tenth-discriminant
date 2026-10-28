"""Synthetic scheduler tests only: these do not invoke Lean or prove mathematics."""
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path
from unittest.mock import patch
import io
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from control_schedule import run_families


class SchedulingTests(unittest.TestCase):
    def test_two_workers_and_all_eight_jobs(self):
        lock = threading.Lock()
        barrier = threading.Barrier(2, timeout=5)
        active = peak = 0
        seen = []
        root = Path.cwd()
        families = [(f'family{i}.py', 120) for i in range(8)]
        def child(command, *, cwd, capture_output, timeout):
            nonlocal active, peak
            self.assertEqual(command[0], sys.executable)
            self.assertEqual(cwd, root)
            self.assertTrue(capture_output)
            self.assertEqual(timeout, 120)
            with lock:
                active += 1
                peak = max(peak, active)
                seen.append(Path(command[1]).name)
            barrier.wait()
            time.sleep(0.01)
            with lock:
                active -= 1
            return subprocess.CompletedProcess(command, 0, b'', b'')
        with patch('control_schedule.subprocess.run', side_effect=child), redirect_stdout(io.StringIO()):
            run_families(root, families)
        self.assertEqual(peak, 2)
        self.assertEqual(active, 0)
        self.assertCountEqual(seen, [name for name, _ in families])

    def test_real_children_outputs_order_and_coverage(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            families = []
            for i in range(8):
                name = f'child{i}.py'
                source = ("from pathlib import Path\nimport sys\n"
                    f"Path(__file__).with_suffix('.ran').write_text('{i}')\n"
                    f"sys.stdout.buffer.write('out{i}:π\\n'.encode('utf-8'))\n"
                    f"sys.stderr.buffer.write(b'err{i}\\n')\n")
                (root/name).write_text(source, encoding='utf-8')
                families.append((name, 10))
            out, err = io.StringIO(), io.StringIO()
            with redirect_stdout(out), redirect_stderr(err):
                run_families(root, families)
            self.assertEqual(len(list(root.glob('*.ran'))), 8)
            self.assertEqual(out.getvalue().count('π'), 8)
            for i in range(8):
                self.assertIn(f'out{i}:π', out.getvalue())
                self.assertIn(f'err{i}', err.getvalue())
            self.assertEqual(sorted(range(8), key=lambda i: out.getvalue().index(f'out{i}:')), list(range(8)))

    def test_nonzero_rejects_and_keeps_diagnostics(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/'bad.py').write_text("import sys\nprint('kept-out')\nprint('kept-err',file=sys.stderr)\nraise SystemExit(7)\n")
            (root/'good.py').write_text("from pathlib import Path\nPath('completed').write_text('yes')\n")
            out, err = io.StringIO(), io.StringIO()
            with redirect_stdout(out), redirect_stderr(err), self.assertRaises(SystemExit) as failure:
                run_families(root, [('bad.py', 10), ('good.py', 10)])
            self.assertIn('exit 7', str(failure.exception))
            self.assertIn('kept-out', out.getvalue())
            self.assertIn('kept-err', err.getvalue())
            self.assertTrue((root/'completed').exists())

    def test_timeout_rejects_and_keeps_partial_output(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/'slow.py').write_text("import time\nprint('before-timeout',flush=True)\ntime.sleep(10)\n")
            out, err = io.StringIO(), io.StringIO()
            with redirect_stdout(out), redirect_stderr(err), self.assertRaises(SystemExit) as failure:
                run_families(root, [('slow.py', 2)])
            self.assertIn('exit 124', str(failure.exception))
            self.assertIn('before-timeout', out.getvalue())
            self.assertIn('TIMEOUT slow.py', err.getvalue())

    def test_launch_error_rejects(self):
        out, err = io.StringIO(), io.StringIO()
        with patch('control_schedule.subprocess.run', side_effect=OSError('synthetic launch failure')):
            with redirect_stdout(out), redirect_stderr(err), self.assertRaises(SystemExit) as failure:
                run_families(Path.cwd(), [('absent.py', 10)])
        self.assertIn('exit 127', str(failure.exception))
        self.assertIn('synthetic launch failure', err.getvalue())

    def test_invalid_jobs_reject_before_launch(self):
        for families in [[], [('a', 1), ('a', 2)], [('a', 0)], [('a', -1)]]:
            with self.subTest(families=families), patch('control_schedule.subprocess.run') as child:
                with self.assertRaises(ValueError):
                    run_families(Path.cwd(), families)
                child.assert_not_called()


if __name__ == '__main__':
    unittest.main(verbosity=2)
