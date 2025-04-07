from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Get the total sum
        total_sum = sum(nums)

        # If the total sum is odd, it can't be partitioned into two equal subsets
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        n = len(nums)

        # Initialize a DP array where dp[i] represents whether we can form sum i
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: we can always form sum 0 (by taking no elements)

        # For each number, update the dp array
        for num in nums:
            # Start from the target and work backwards to avoid using the same element multiple times
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[target]

# Example usage:
nums = [1, 5, 11, 5]
solution = Solution()
result = solution.canPartition(nums)
print(f"Can the array {nums} be partitioned into two equal sum subsets? {result}")