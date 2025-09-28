from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i + 1], nums[i + 2]
            if b + c > a:
                return a + b + c
        return 0

solution = Solution()

nums1 = [2, 1, 2]
result1 = solution.largestPerimeter(nums1)
print(f"The list is {nums1}")
print(f"The largest perimeter is: {result1}")


nums2 = [1, 2, 10]
result2 = solution.largestPerimeter(nums2)
print(f"\nThe list is {nums2}")
print(f"The largest perimeter is: {result2}")


