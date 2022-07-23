import unittest
from .main import get_logger

class TestLogger(unittest.TestCase):
    
    def test_check_init(self):
        logger = get_logger()
        logger.info("123")