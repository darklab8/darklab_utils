
import unittest
from .main import EnumWithValues, auto

auto_action = auto


class _EnumForTests(EnumWithValues):
    example1 = auto_action()
    example2 = auto_action()
    
class TestEnum(unittest.TestCase):
    
    def setUp(self):
        self.instance = _EnumForTests

    def test_i_get_value(self):
        self.assertEqual(self.instance.example1, "example1")

    def test_i_get_keys(self):
        self.assertEqual(self.instance.get_keys(), ["example1", "example2"])
