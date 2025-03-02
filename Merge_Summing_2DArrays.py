from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        merged = {}

        # Add values from nums1
        for id1, val1 in nums1:
            merged[id1] = merged.get(id1, 0) + val1

        # Add values from nums2
        for id2, val2 in nums2:
            merged[id2] = merged.get(id2, 0) + val2

        # Convert merged dictionary to sorted list of [id, value]
        result = sorted(merged.items())

        # Format as required [[id, value], ...]
        return [[id, val] for id, val in result]


if __name__ == "__main__":
    solution = Solution()
    nums1 = [[1, 2], [2, 3], [4, 5]]
    nums2 = [[1, 4], [3, 2], [4, 1]]
    result = solution.mergeArrays(nums1, nums2)
    print("Merged array:", result)
