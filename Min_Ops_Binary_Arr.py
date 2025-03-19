from typing import List


class Solution:
  def minOperations(self, nums: List[int]) -> int:
    n = len(nums)
    if n < 3:
      return -1
    operations = 0
    for i in range(n - 2):
      if nums[i] == 0:
        operations += 1
        for j in range(i, i + 3):
          if j < n:
            nums[j] = 1 - nums[j]
    if nums[n - 2] == 0 or nums[n - 1] == 0:
      return -1
    return operations

# Example Usage:

# Create an object of the Solution class
solution_object = Solution()

# Example 1: nums = [0, 1, 1, 1, 0, 0]
nums1 = [0, 1, 1, 1, 0, 0]
result1 = solution_object.minOperations(nums1)
print(f"For nums = {nums1}, the minimum operations required are: {result1}")

# Example 2: nums = [0, 1, 1, 1]
nums2 = [0, 1, 1, 1]
result2 = solution_object.minOperations(nums2)
print(f"For nums = {nums2}, the minimum operations required are: {result2}")

# Let's take another example to see the in-place modification
nums3 = [0, 0, 0, 1, 1, 1]
print(f"Initial nums3: {nums3}")
result3 = solution_object.minOperations(nums3)
print(f"For nums = {nums3}, the minimum operations required are: {result3}")
print(f"Final nums3: {nums3}") # Notice how nums3 is modified in place

# Example with an array that is already all 1s
nums4 = [1, 1, 1, 1, 1]
result4 = solution_object.minOperations(nums4)
print(f"For nums = {nums4}, the minimum operations required are: {result4}")

# Example where it might be impossible (based on our logic)
nums5 = [0, 1, 0]
result5 = solution_object.minOperations(nums5)
print(f"For nums = {nums5}, the minimum operations required are: {result5}")