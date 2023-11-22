# test_edit_distance.py

import unittest

from edit_distance import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        print("Setting up test...")

    def tearDown(self):
        print("Tearing down test...")

    def test_min_distance_same_words(self):
        result = self.solution.minDistance("word", "word")
        self.assertEqual(result, 0)

    def test_min_distance_one_empty_word(self):
        result = self.solution.minDistance("hello", "")
        self.assertEqual(result, 5)

    def test_min_distance_insert_operations(self):
        result = self.solution.minDistance("kitten", "sitting")
        self.assertEqual(result, 3)

    def test_min_distance_replace_operations(self):
        result = self.solution.minDistance("intention", "execution")
        self.assertEqual(result, 5)

    def test_min_distance_assert_false(self):
        result = self.solution.minDistance("abc", "xyz")
        self.assertFalse(
            result == 0, "Distance between 'abc' and 'xyz' should not be 0."
        )

    def test_min_distance_assert_raises(self):
        with self.assertRaises(TypeError):
            self.solution.minDistance("abc", 123)

    def test_min_distance_enter_context(self):
        with self.subTest(msg="Testing distance between 'hello' and 'world'"):
            result = self.solution.minDistance("hello", "world")
            self.assertEqual(result, 4)

        with self.subTest(msg="Testing distance between 'open' and 'closed'"):
            result = self.solution.minDistance("open", "closed")
            self.assertEqual(result, 4)

    def test_min_distance_fail(self):
        result = self.solution.minDistance("abc", "xyz")
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
