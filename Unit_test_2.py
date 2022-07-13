import unittest
import Unit_test_1

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = Unit_test_1.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_two_word(self):
        text = 'monty python'
        result = Unit_test_1.cap_text(text)
        self.assertEqual(result, 'Monty Python')

if __name__ == '__main__':
    unittest.main()
