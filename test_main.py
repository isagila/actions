import unittest
from main import *


class MyTestCase(unittest.TestCase):

    def test_check_args(self):
        self.assertEqual(check_args(["1", "2"]), True)
        self.assertEqual(check_args(["1", "2", "3"]), False)
        self.assertEqual(check_args(["1"]), False)
        self.assertEqual(check_args(["a", "b"]), False)
        self.assertEqual(check_args(["a", "1"]), False)
        self.assertEqual(check_args(["1", "b"]), False)

    def test_parse_equation(self):
        self.assertEqual(parse_equation("1+2"), ("+", ["1", "2"]))
        self.assertEqual(parse_equation("1 +2"), ("+", ["1", "2"]))
        self.assertEqual(parse_equation("1 + 2"), ("+", ["1", "2"]))
        self.assertEqual(parse_equation("1 + 2\n"), ("+", ["1", "2"]))
        self.assertEqual(parse_equation("1+ 2\n"), ("+", ["1", "2"]))
        self.assertEqual(parse_equation("11 -   2\n"), ("-", ["11", "2"]))
        self.assertEqual(parse_equation("11*  1"), ("*", ["11", "1"]))
        self.assertEqual(parse_equation("5  /  0"), ("/", ["5", "0"]))
        self.assertEqual(parse_equation("5 3"), ("", ["5 3"]))
        self.assertEqual(parse_equation("5 ^ 5"), ("", ["5 ^ 5"]))
        self.assertEqual(parse_equation(""), ("", []))

    def test_calculate(self):
        self.assertEqual(calculate("21* 2"), 42)
        self.assertEqual(calculate("42 - 0"), 42)
        self.assertEqual(calculate("0 + 42"), 42)
        self.assertEqual(calculate("462 / 11"), 42)
        self.assertEqual(calculate("17+ 25"), 42)
        self.assertEqual(calculate("41   +1\n"), 42)
        self.assertRaises(Exception, lambda: calculate("42 / 0"))
        self.assertRaises(Exception, lambda: calculate("42 42"))
        self.assertRaises(Exception, lambda: calculate("42 & 42"))
        self.assertRaises(Exception, lambda: calculate("1 + 3 + 3 "))
        self.assertRaises(Exception, lambda: calculate(""))


if __name__ == "__main__":
    unittest.main()
