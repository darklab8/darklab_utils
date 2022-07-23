import unittest
import os
from .main import EnvReader

class TestEnvReader(unittest.TestCase):
    
    def setUp(self):
        self.env_reader = EnvReader()
        os.environ["TEST_VAR"] = "123"

    def test_i_can_get_var(self):
        self.assertEqual(self.env_reader["TEST_VAR"], "123")

    def test_i_get_default_if_value_does_not_exist(self):
        self.assertEqual(self.env_reader.get("NOT_EXISTING_VAR", "456"), "456")

    def test_u_get_exception_for_non_existing_value(self):
        with self.assertRaises(KeyError) as context:
            self.env_reader["NOT_EXISTING_VAR"]

        self.assertTrue("NOT_EXISTING_VAR" in str(context.exception))
        self.assertTrue(isinstance(context.exception, KeyError))