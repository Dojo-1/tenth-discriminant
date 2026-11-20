"""Phase371 public task identity and initial no-credit controls."""
import sys
from pathlib import Path
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parent))
from task_probe import task_fields,task_id,probe,REF
HEAD="a"*40
def env(attempt="1"):
    return {"GITHUB_SHA":HEAD,"GITHUB_REF":REF,
            "GITHUB_RUN_ID":"812345","GITHUB_RUN_ATTEMPT":attempt}
class ProbeContract(unittest.TestCase):
    def test_sha_binding(self):
        self.assertNotEqual(task_id(HEAD),task_id("b"*40))
        self.assertEqual(task_id(HEAD),task_id(HEAD))
    def test_source_fixed(self):
        self.assertEqual(task_fields(HEAD)["source"],
            "original-integer-pair-ordinary-Z-gram@phase367")
        self.assertEqual(task_fields(HEAD)["scope"],"source_contract")
    def test_initial_push_not_receipt(self):
        self.assertEqual(probe(env()),"PHASE371_INITIAL_PUSH_NOT_ISSUED_NO_CREDIT")
    def test_wrong_ref(self):
        d=env();d["GITHUB_REF"]="refs/heads/main"
        with self.assertRaises(ValueError): probe(d)
    def test_short_sha(self):
        d=env();d["GITHUB_SHA"]="a"*39
        with self.assertRaises(ValueError):probe(d)
    def test_bad_run_id(self):
        d=env();d["GITHUB_RUN_ID"]="bad"
        with self.assertRaises(ValueError):probe(d)
    def test_zero_attempt(self):
        with self.assertRaises(ValueError):probe(env("0"))
if __name__=="__main__":
    unittest.main()
