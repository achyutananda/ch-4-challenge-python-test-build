"""Unit tests for hello.py"""
import unittest
from unittest.mock import patch
import hello


class TestHello(unittest.TestCase):
    """Test cases for hello module."""

    def test_hello_output(self):
        """Test that hello() prints Hello, World!"""
        with patch("builtins.print") as mock_print:
            hello.hello()
            mock_print.assert_called_once_with("Hello, World!")

    def test_hello_called_once(self):
        """Test that print is called exactly once."""
        with patch("builtins.print") as mock_print:
            hello.hello()
            self.assertEqual(mock_print.call_count, 1)


if __name__ == "__main__":
    unittest.main()
