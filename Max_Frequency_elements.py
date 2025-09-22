from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        if not nums:
            return 0

        freq = [0] * 101

        for num in nums:
            freq[num] += 1

        max_f = max(freq)

        count = 0
        for f in freq:
            if f == max_f:
                count += 1

        return count * max_f


solution = Solution()

nums1 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(solution.maxFrequencyElements(nums1))

nums2 = [5]
print(solution.maxFrequencyElements(nums2))

nums3 = [10, 20, 30, 40, 50]
print(solution.maxFrequencyElements(nums3))

nums4 = []
print(solution.maxFrequencyElements(nums4))

nums5 = [2, 2, 3, 3, 3, 3, 5, 5]
print(solution.maxFrequencyElements(nums5))
