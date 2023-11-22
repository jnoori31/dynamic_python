import unittest

from longest_increasing_subsequence import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        # Initialize your testing setup if needed
        pass

    def tearDown(self):
        # Clean up resources if needed
        pass

    def test_length_of_lis_pass(self):
        # Test case where the function should pass
        solution = Solution()
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        result = solution.LengthOfLIS(nums)
        print(f"Test length_of_lis_pass Result: {result}")
        self.assertEqual(result, 4)  # Update to the correct expected result

    def test_length_of_lis_fail(self):
        # Test case where the function should fail
        solution = Solution()
        nums = [3, 2, 1, 0, 4]

        result = solution.LengthOfLIS(nums)
        expected_result = 4
        print(f"Test length_of_lis_fail Result: {result}")

        if result != expected_result:
            print(f"Fail: Expected {expected_result}, but got {result}")

        self.assertNotEqual(
            result, expected_result
        )  # Update to the correct expected result

    def test_length_of_lis_empty_list(self):
        # Test case where nums is an empty list, leading to a ValueError
        solution = Solution()
        nums = []

        try:
            result = solution.LengthOfLIS(nums)
            print(f"Test length_of_lis_empty_list Result: {result}")
        except ValueError as e:
            print(f"Test length_of_lis_empty_list Result: {e}")

    def test_length_of_lis_single_element(self):
        # Test case with a single element list
        solution = Solution()
        nums = [5]
        result = solution.LengthOfLIS(nums)
        print(f"Test length_of_lis_single_element Result: {result}")
        self.assertEqual(result, 1)

    def test_length_of_lis_duplicates(self):
        # Test case with a list containing duplicates
        solution = Solution()
        nums = [3, 2, 3, 1, 4]
        result = solution.LengthOfLIS(nums)
        # Expected result can be either [2, 3, 4] or [1, 3, 4]
        print(f"Test length_of_lis_duplicates Result: {result}")
        self.assertIn(result, [3, 4])

    def test_length_of_lis_descending_order(self):
        # Test case with a list in descending order
        solution = Solution()
        nums = [5, 4, 3, 2, 1]
        result = solution.LengthOfLIS(nums)
        print(f"Test length_of_lis_descending_order Result: {result}")
        self.assertEqual(result, 1)

    def test_length_of_lis_negative_numbers(self):
        # Test case with a list containing negative numbers
        solution = Solution()
        nums = [3, -2, 5, -1, 2]
        result = solution.LengthOfLIS(nums)
        # Expected result can be either [3, 5] or [3, 5, 2]
        print(f"Test length_of_lis_negative_numbers Result: {result}")
        self.assertIn(result, [2, 3])

    def test_length_of_lis_floating_point_numbers(self):
        # Test case with a list containing floating-point numbers
        solution = Solution()
        nums = [1.5, 2.0, 1.0, 2.5]
        result = solution.LengthOfLIS(nums)
        # Expected result depends on how floating-point numbers are handled
        print(f"Test length_of_lis_floating_point_numbers Result: {result}")
        self.assertTrue(result >= 1)

    def test_length_of_lis_type_error(self):
        # Test case where nums contains a string, leading to a TypeError
        solution = Solution()
        nums = [1, 2, 3, "fairy", 5]  # Incorrect: includes a non-integer

        try:
            result = solution.LengthOfLIS(nums)
            print(f"Test length_of_lis_type_error Result: {result}")
        except TypeError as e:
            print(f"Test length_of_lis_type_error Result: {e}")


if __name__ == "__main__":
    unittest.main()

# results of test (pytest -s test_longest_increasing_subsequence.py)
