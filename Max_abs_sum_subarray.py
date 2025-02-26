from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = 0
        min_sum = 0
        current_max = 0
        current_min = 0

        for num in nums:
            current_max = max(0, current_max + num)
            current_min = min(0, current_min + num)
            max_sum = max(max_sum, current_max)
            min_sum = min(min_sum, current_min)

        return max(max_sum, abs(min_sum))

nums = [1, -3, 2, 3, -4]
solution = Solution()
result = solution.maxAbsoluteSum(nums)
print(f"Maximum Absolute Sum of Subarray: {result}")