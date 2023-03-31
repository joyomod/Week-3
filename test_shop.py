import unittest
import unittest
from shop import *
from unittest.mock import patch


class TestShop(unittest.TestCase):
    # test list of items displayed
    def test_display_items(self, mock_stdout):
        purchase_or_exit()
        expected_output = "Item: T-shirt, Price: 19.99\nItem: Hoodie, Price: 39.99\nItem: Cap, Price: 14.99\nItem: " \
                          "Mug, Price: 9.99\nItem: Keychain, Price: 5.99\nItem: Poster, Price: 12.99\nItem: Sticker, " \
                          "Price: 2.99\nItem: Phone Case, Price: 24.99\nItem: Backpack, Price: 49.99\nItem: Water " \
                          "Bottle, Price: 17.99\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    # Test 'exit' input by user
    def test_exit(self):
        with patch('builtins.input', return_value='exit'):
            with self.assertRaises(SystemExit):
                purchase_or_exit()
