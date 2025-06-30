from typing import List
from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:

        freq = Counter(nums)

        max_length = 0

        # For each unique number, check if num+1 exists
        for num in freq:
            if num + 1 in freq:
                # Harmonious subsequence length is count of num + count of num+1
                current_length = freq[num] + freq[num + 1]
                max_length = max(max_length, current_length)

        return max_length

    def findLHS_with_details(self, nums: List[int]) -> tuple:

        freq = Counter(nums)
        max_length = 0
        pairs_found = []
        best_pair = None

        for num in sorted(freq.keys()):
            if num + 1 in freq:
                current_length = freq[num] + freq[num + 1]
                pair_info = {
                    'values': (num, num + 1),
                    'counts': (freq[num], freq[num + 1]),
                    'total_length': current_length
                }
                pairs_found.append(pair_info)

                if current_length > max_length:
                    max_length = current_length
                    best_pair = pair_info

        return max_length, pairs_found, best_pair


def demonstrate_basic_examples():

    solution = Solution()

    print("=== Basic Examples ===")

    # Example 1
    nums1 = [1, 3, 2, 2, 5, 2, 3, 7]
    result1 = solution.findLHS(nums1)
    print(f"Input: {nums1}")
    print(f"Output: {result1}")
    print(f"Explanation: Harmonious subsequence [3,2,2,2,3] has length {result1}")
    print()

    # Example 2
    nums2 = [1, 2, 3, 4]
    result2 = solution.findLHS(nums2)
    print(f"Input: {nums2}")
    print(f"Output: {result2}")
    print(f"Explanation: Multiple harmonious subsequences of length {result2}")
    print()

    # Example 3
    nums3 = [1, 1, 1, 1]
    result3 = solution.findLHS(nums3)
    print(f"Input: {nums3}")
    print(f"Output: {result3}")
    print(f"Explanation: No harmonious subsequence exists")
    print()


if __name__ == "__main__":
    print("Longest Harmonious Subsequence - Complete Implementation\n")

    # Run all demonstrations
    demonstrate_basic_examples()
