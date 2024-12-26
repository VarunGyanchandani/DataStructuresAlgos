def findTargetSumWays(nums, target):
    # Calculate the sum of the numbers in the array
    total_sum = sum(nums)

    # If the target is out of range, there's no way to achieve it
    if abs(target) > total_sum:
        return 0

    # We shift all possible sums by total_sum to make them non-negative
    # We are effectively working in a range of [0, 2 * total_sum]
    dp = [0] * (2 * total_sum + 1)
    dp[total_sum] = 1  # base case: one way to achieve sum 0 (index total_sum)

    for num in nums:
        next_dp = [0] * (2 * total_sum + 1)
        for sum_so_far in range(len(dp)):
            if dp[sum_so_far] > 0:
                # We can either add num or subtract num
                next_dp[sum_so_far + num] += dp[sum_so_far]
                next_dp[sum_so_far - num] += dp[sum_so_far]
        dp = next_dp

    # We need to return the number of ways to achieve the target sum
    return dp[total_sum + target]  # shift the target by total_sum


# Example usage:
nums1 = [1, 1, 1, 1, 1]
target1 = 3
print(findTargetSumWays(nums1, target1))  # Output: 5

nums2 = [1]
target2 = 1
print(findTargetSumWays(nums2, target2))  # Output: 1
