import unittest
from unittest.mock import patch
from io import StringIO
import sys
from console import HBNBCommand


class TestCreateCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def test_create_with_string_param(self):
        # Test creating an object with string parameters
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create State name=\"California\"")
            output = fake_out.getvalue().strip()
            self.assertTrue(output)

    def test_create_with_float_param(self):
        # Test creating an object with float parameters
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create Place number_rooms=4.5")
            output = fake_out.getvalue().strip()
            self.assertTrue(output)

    def test_create_with_integer_param(self):
        # Test creating an object with integer parameters
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create Place max_guest=10")
            output = fake_out.getvalue().strip()
            self.assertTrue(output)

    def test_create_with_invalid_param(self):
        # Test creating an object with invalid parameters
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create Place invalid_param=invalid_value")
            output = fake_out.getvalue().strip()
            self.assertFalse(output)


if __name__ == '__main__':
    unittest.main()
