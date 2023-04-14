import unittest
from isogram import is_isogram


class TestIsogram(unittest.TestCase):
    # Test case 1: Testing if a string no repeated letters is an isogram - it is a positive test to respond
    # to when the input is indeed an isogram
    def test_is_isogram(self):
        self.assertEqual(is_isogram("abcdefg"), True)

    # Test case 2: Testing if a string with repeated letters is not an isogram - it is a negative test to respond
    # to when the input is not an isogram
    def test_is_not_isogram(self):
        self.assertEqual(is_isogram("hello"), False)

    # Test case 3: Testing if a string with repeated letters but with has a mixture of lower and upper case letters is an isogram
    def test_is_mixed_case(self):
        self.assertEqual(is_isogram("HeLlO"), False)

    # Test case 4: Testing if a string with only one character is an isogram - this is a positive test as it has only one count
    def test_is_one_letter(self):
        self.assertEqual(is_isogram("a"), True)

    # Test case 5:  Testing if a string with special characters is an isogram
    def test_is_special_char(self):
        self.assertEqual(is_isogram("hello, world!"), False)


if __name__ == '__main__':
    unittest.main()
