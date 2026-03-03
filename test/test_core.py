#!/usr/bin/env python3
"""
Tests for ``moke.core``
"""
import unittest
import moke.core
import os
from moke.util import run_app

_TEST_DIR = os.path.dirname(os.path.abspath(__file__))
_SCRIPTS_DIR = os.path.join(_TEST_DIR, "scripts")

class Test_core(unittest.TestCase):

    def test_path(self):
        assert moke.util.path

    def setUp(self):
        self._orig_cwd = os.getcwd()
        os.chdir(_SCRIPTS_DIR)

    def tearDown(self):
        os.chdir(self._orig_cwd)

    def test_run0_no_mokefile(self):
        os.chdir(_TEST_DIR)
        ret, out, err, cmd = run_app("moke")
        assert ret == 1
        assert out == b""
        assert err

    def test_run1_no_subcommand(self):
        ret, out, err, cmd = run_app("moke")
        assert ret == 2
        assert out == b""
        assert err

    def test_run2_usage_message(self):
        ret, out, err, cmd = run_app("moke")
        assert ret == 2
        assert out == b""
        assert b"usage: mokefile.py" in err

    def test_grop1_no_args(self):
        ret, out, err, cmd = run_app("./grop.py")
        assert ret == 2
        assert out == b""
        assert b"usage: grop.py" in err
        assert cmd == './grop.py'

    def test_grop2_pattern_match(self):
        ret, out, err, cmd = run_app(r'cat ../data/grop.inp | ./grop.py ".*\(\d{2}\).*"')
        assert out == b"a line with a number (42)\n"
        assert ret == 0

    def test_mf1_fromdef_int(self):
        ret, out, err, cmd = run_app("moke fromdef_int")
        assert ret == 0

    def test_mf2_fromdef_float(self):
        ret, out, err, cmd = run_app("moke fromdef_float")
        assert ret == 0

    def test_mf3_fromdef_path_r(self):
        ret, out, err, cmd = run_app("echo 1 | moke fromdef_path_r")
        assert ret == 0

    def test_mf4_fromdef_path_w(self):
        ret, out, err, cmd = run_app("echo 1 | moke fromdef_path_w")
        assert ret == 0

    def test_mf5_fromdoc_none_int(self):
        ret, out, err, cmd = run_app("moke fromdoc_none_int -i 10")
        assert ret == 0, err


if __name__ == "__main__":
    unittest.main()
