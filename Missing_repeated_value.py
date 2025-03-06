from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        count = [0] * (n * n + 1)

        # Count occurrences of each number in the grid
        for row in grid:
            for num in row:
                count[num] += 1

        repeated = -1
        missing = -1

        # Find the repeated and missing values
        for num in range(1, n * n + 1):
            if count[num] == 2:
                repeated = num
            elif count[num] == 0:
                missing = num

            if repeated != -1 and missing != -1:
                break

        return [repeated, missing]


# Example usage
grid = [[1, 3], [2, 2]]
solution = Solution()
print(solution.findMissingAndRepeatedValues(grid))  # Output: [2, 4]

grid = [[9, 1, 7], [8, 9, 2], [3, 4, 6]]
print(solution.findMissingAndRepeatedValues(grid))  # Output: [9, 5]
