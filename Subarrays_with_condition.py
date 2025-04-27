from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)

        print(f"Array: {nums}")
        print("Checking all subarrays of length 3...")

        for i in range(n - 2):
            subarray = nums[i:i + 3]
            first, middle, third = subarray

            print(f"Subarray {i}: {subarray}")
            print(f"  Checking if {first} + {third} = {middle}/2")

            if first + third == middle / 2:
                print(f"  ✓ Condition met: {first} + {third} = {middle / 2}")
                count += 1
            else:
                print(f"  ✗ Condition not met: {first} + {third} ≠ {middle / 2}")

        print(f"Total count of valid subarrays: {count}")
        return count


# Example 1
nums1 = [1, 2, 1, 4, 1]
solution = Solution()
print("\nExample 1:")
result1 = solution.countSubarrays(nums1)
print("\nFinal result:", result1)

# Example 2
nums2 = [1, 1, 1]
print("\nExample 2:")
result2 = solution.countSubarrays(nums2)
print("\nFinal result:", result2)

# Additional Example
nums3 = [2, 6, 4, 8, 10, 2]
print("\nAdditional Example:")
result3 = solution.countSubarrays(nums3)
print("\nFinal result:", result3)