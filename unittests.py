#!/usr/bin/python3
import unittest
from sys import argv
from os import environ

try:
    import common
except ImportError:
    print("Failed to import common! Does it exist? Is it in the same folder as this script? Am I going insane?")
    exit(1)



class TestCommon(unittest.TestCase):
    """
    Make sure the common library works
    """

    def test_validate_int_to_int(self):
        result = common.validateInteger(5)
        self.assertEqual(result, 5)
    
    @unittest.skipUnless("MATHING_NOSKIPTEST" in dict(environ).keys() and dict(environ)["MATHING_NOSKIPTEST"] == "1", "Not fully implemented yet")
    def test_validate_float_to_int(self):
        result = common.validateInteger(5.5)
        self.assertEqual(result, 55)

if __name__ == "__main__":
    unittest.main()