import unittest
from shop import purchase_or_exit
from unittest.mock import patch
from io import StringIO
import sys


class TestShop(unittest.TestCase):
    # tests welcome message
    def test_welcome_message(self):
        with patch('builtins.input', return_value='exit'):
            captured_output = StringIO()
            sys.stdout = captured_output
            customer_name = 'Jonny'
            expected_output = f'Hi {customer_name}, welcome to the CFG merch store\nPlease see the list of items on sale and the respective prices\n'
            purchase_or_exit()
            self.assertEqual(captured_output.getvalue(), expected_output)

    # test the displayed items
    def test_display_items(self):
        with patch('builtins.input', return_value='exit'):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                purchase_or_exit()
                expected_output = "Item: T-shirt, Price: 19.99\nItem: Hoodie, Price: 39.99\nItem: Cap, Price: 14.99\nItem: " \
                                  "Mug, Price: 9.99\nItem: Keychain, Price: 5.99\nItem: Poster, Price: 12.99\nItem: Sticker, " \
                                  "Price: 2.99\nItem: Phone Case, Price: 24.99\nItem: Backpack, Price: 49.99\nItem: Water " \
                                  "Bottle, Price: 17.99\n"
                self.assertEqual(mock_stdout.getvalue(), expected_output)

    # tests "exit" from user input
    def test_exit(self):
        with patch('builtins.input', return_value='exit'):
            with self.assertRaises(SystemExit):
                purchase_or_exit()


if __name__ == '__main__':
    unittest.main()
