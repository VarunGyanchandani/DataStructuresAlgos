class Solution:
    def minCapability(self, nums: list[int], k: int) -> int:
        def can_steal(capability: int) -> bool:
            count = 0
            prev_stolen = False
            for num in nums:
                if num <= capability and not prev_stolen:
                    count += 1
                    prev_stolen = True
                else:
                    prev_stolen = False
            return count >= k

        left, right = min(nums), max(nums)
        while left < right:
            mid = left + (right - left) // 2
            if can_steal(mid):
                right = mid
            else:
                left = mid + 1
        return left

# Example Usage
nums1 = [2, 3, 5, 9]
k1 = 2
solution = Solution()
result1 = solution.minCapability(nums1, k1)
print(f"Example 1: nums = {nums1}, k = {k1}, Minimum Capability = {result1}")

nums2 = [2, 7, 9, 3, 1]
k2 = 2
result2 = solution.minCapability(nums2, k2)
print(f"Example 2: nums = {nums2}, k = {k2}, Minimum Capability = {result2}")

nums3 = [2, 10, 5, 20, 1]
k3 = 3
result3 = solution.minCapability(nums3, k3)
print(f"Example 3: nums = {nums3}, k = {k3}, Minimum Capability = {result3}")

nums4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k4 = 5
result4 = solution.minCapability(nums4, k4)
print(f"Example 4: nums = {nums4}, k = {k4}, Minimum Capability = {result4}")