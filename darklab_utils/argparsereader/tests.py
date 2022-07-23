import unittest
from .main import ArgparseReader

class TestCliReader(unittest.TestCase):

    def setUp(self):
        self.instance = ArgparseReader()

    def _read_args(self, cli_reader, args):
        return cli_reader.get_data(args=args, ignore_others=False)

    def test_help(self):
        self._read_args(self.instance,"")

    def test_register_and_read_arguments(self):
        instance = self.instance
        instance = instance.add_argument("--argument", type=int)
        args = self._read_args(instance, ["--argument=123"])
        self.assertEqual(args.argument, 123)

    def test_ignore_unregistered(self):
        with self.assertRaises(SystemExit) as context:
            args = self._read_args(self.instance, ["--argument=123"])

        self.assertTrue(isinstance(context.exception, SystemExit))
    
    def test_get_data(self):
        instance = self.instance.add_argument("--argument", type=int)
        args = self._read_args(instance, ["--argument=123"])

        self.assertEqual(args.get_as_dict(), {'argument': 123})