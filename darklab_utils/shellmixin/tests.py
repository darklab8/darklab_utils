import unittest
from .main import _shell_execute, ShellException

class TestShellMixin(unittest.TestCase):

    def test_get_good_cmd_command(self):
        _shell_execute("echo 123")

    def test_wrong_cmd_command(self):
        with self.assertRaises(ShellException) as context:
            _shell_execute("mkdir 1/2/3/6/5/7")

        self.assertTrue(isinstance(context.exception, ShellException))