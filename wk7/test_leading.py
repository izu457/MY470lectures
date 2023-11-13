import unittest
import leading

#We should test the programm for one character strings,
# two characters, more than two characters, integers, and
# empty strings.

class TestLeasing(unittest.TestCase):
    "Tests the program in leading.py"

    def test_one_character(self):
        inputted = ["a"]
        leading.leading_substrings(inputted)
        output_expected = ["a"]
        self.assertEqual(inputted, output_expected)

    def test_two_characters(self):
        inputted = ["ab"]
        leading.leading_substrings(inputted)
        output_expected = ["a", "ab"]
        self.assertEqual(inputted, output_expected)
#more functions needed

if __name__ == '__main__':
    unittest.main()