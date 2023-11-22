import unittest

from longest_common_subsequence import LongestCommonSubsequence


class TestLongestCommonSubsequence(unittest.TestCase):
    def setUp(self):
        # Initialize your testing setup if needed
        pass

    def tearDown(self):
        # Clean up resources if needed
        pass

    def test_longest_common_subsequence_pass(self):
        # Test case where the function should pass
        text1 = "abcde"
        text2 = "ace"
        result = LongestCommonSubsequence(text1, text2)
        self.assertEqual(result, 3)

    def test_longest_common_subsequence_fail(self):
        # Test case where the function should fail
        text1 = "abc"
        text2 = "def"
        result = LongestCommonSubsequence(text1, text2)
        self.assertNotEqual(result, 2)  # Replace 2 with the expected result

    def test_longest_common_subsequence_empty_strings(self):
        # Test case with empty strings
        text1 = ""
        text2 = ""
        result = LongestCommonSubsequence(text1, text2)
        self.assertEqual(result, 0)

    def test_longest_common_subsequence_one_empty_string(self):
        # Test case with one empty string
        text1 = "abc"
        text2 = ""
        result = LongestCommonSubsequence(text1, text2)
        self.assertEqual(result, 0)

    def test_longest_common_subsequence_spaces(self):
        # Test case with spaces
        text1 = "ab cde"
        text2 = "a c e"
        result = LongestCommonSubsequence(text1, text2)
        self.assertEqual(result, 4)


if __name__ == "__main__":
    unittest.main()
