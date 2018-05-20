#!/usr/bin/python3
import unittest
from sys import argv
from os import environ

try:
    import common
except ImportError:
    print("Failed to import common! Does it exist? Is it in the same folder as this script? Am I going insane?")
    exit(1)

noskip = False
# If MATHING_NOSKIPTEST (env var) exists and is 1
if "MATHING_NOSKIPTEST" in dict(environ).keys() and dict(environ)["MATHING_NOSKIPTEST"] == "1":
    noskip = True


class TestCommon(unittest.TestCase):
    """
    Make sure the common library works
    """

    # common.validateInteger
    def test_validate_int_to_int(self):
        result = common.validateInteger(5)
        self.assertEqual(result, 5)

    def test_validate_int_in_string_to_int(self):
        result = common.validateInteger("5")
        self.assertEqual(result, 5)
    
    def test_validate_bad_int_in_string_to_int(self):
        result = common.validateInteger("efhweh5eih,/!#$%^&*()-_[];:")
        self.assertEqual(result, 5)

    @unittest.skipUnless(noskip, "Not properly handled yet")
    def test_validate_float_to_int(self):
        result = common.validateInteger(5.5)
        self.assertEqual(result, 55)    

    def test_validate_empty_string_to_int(self):
        result = common.validateInteger("")
        self.assertEqual(result, 0)

    def test_validate_None_to_int(self):
        result = common.validateInteger(None)
        self.assertEqual(result, 0)


    # common.validateFloat    
    def test_validate_float_to_float(self):
        result = common.validateFloat(5.5)
        self.assertEqual(result, 5.5)

    def test_validate_float_in_string_to_float(self):
        result = common.validateFloat("5.5")
        self.assertEqual(result, 5.5)

    def test_validate_bad_float_in_string_to_float(self):
        result = common.validateFloat("fdsfd5gth.uhhjk5ccbnn")
        self.assertEqual(result, 5.5)

    def test_validate_double_decimal_float_in_string_to_float(self):
        result = common.validateFloat("5.5.5")
        self.assertEqual(result, 5.55)

if __name__ == "__main__":
    unittest.main()