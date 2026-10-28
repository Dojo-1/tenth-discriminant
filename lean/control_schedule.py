"""Run independent control families with bounded concurrency and complete diagnostics."""
from concurrent.futures import ThreadPoolExecutor
import subprocess
import sys


def _emit(data, stream):
    if not data:
        return
    if hasattr(stream, 'buffer'):
        stream.buffer.write(data)
    else:
        stream.write(data.decode('utf-8', errors='replace'))
    stream.flush()


def _run(root, family):
    name, timeout = family
    command = [sys.executable, str(root / name)]
    try:
        result = subprocess.run(command, cwd=root, capture_output=True, timeout=timeout)
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired as error:
        return 124, error.stdout or b'', (error.stderr or b'') + f'\nTIMEOUT {name}: {timeout}s\n'.encode()
    except OSError as error:
        return 127, b'', f'LAUNCH_ERROR {name}: {error}\n'.encode()


def run_families(root, families):
    """All families must pass; captured output is reported in declaration order."""
    families = tuple(families)
    if not families or len({name for name, _ in families}) != len(families):
        raise ValueError('Control families must be nonempty and distinct')
    if any(timeout <= 0 for _, timeout in families):
        raise ValueError('Every control family needs a positive timeout')
    failures = []
    priority = sorted(families, key=lambda family: -family[1])
    with ThreadPoolExecutor(max_workers=2) as pool:
        results = {name: pool.submit(_run, root, (name, timeout))
                   for name, timeout in priority}
        for name, _ in families:
            code, stdout, stderr = results[name].result()
            _emit(stdout, sys.stdout)
            _emit(stderr, sys.stderr)
            if code:
                failures.append(f'{name}: exit {code}')
            else:
                print(f'CONTROL_FAMILY_OK {name}', flush=True)
    if failures:
        raise SystemExit('Control family failure: ' + '; '.join(failures))
