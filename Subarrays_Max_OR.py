from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # next_pos[b] = next index ≥ i where bit b is set; init to -1
        next_pos = [-1] * 31
        ans = [1] * n

        # scan from right to left
        for i in range(n - 1, -1, -1):
            x = nums[i]
            # update next positions for bits in nums[i]
            for b in range(31):
                if (x >> b) & 1:
                    next_pos[b] = i

            # determine the farthest index we must reach to cover all bits
            farthest = i
            for b in range(31):
                if next_pos[b] != -1:
                    farthest = max(farthest, next_pos[b])

            ans[i] = farthest - i + 1

        return ans


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        [1, 0, 2, 1, 3],
        [1, 2],
        [0, 0, 0],        # all zeros → OR stays 0, so length is always 1
        [5, 1, 3, 7, 2],  # mixed bits
    ]

    for nums in test_cases:
        result = sol.smallestSubarrays(nums)
        print(f"nums = {nums}\n→ smallestSubarrays = {result}\n")
