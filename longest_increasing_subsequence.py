class Solution:
    def LengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            raise ValueError("Input list 'nums' cannot be empty.")

        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)
        return max(LIS)

