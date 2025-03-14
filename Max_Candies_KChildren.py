from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0

        left, right = 1, max(candies)

        def can_allocate(mid: int) -> bool:
            count = sum(c // mid for c in candies)
            return count >= k

        while left < right:
            mid = (left + right + 1) // 2
            if can_allocate(mid):
                left = mid
            else:
                right = mid - 1

        return left


# Example usage
if __name__ == "__main__":
    solution = Solution()
    candies = [5, 8, 6]
    k = 3
    print(solution.maximumCandies(candies, k))

    candies = [2, 5]
    k = 11
    print(solution.maximumCandies(candies, k))
