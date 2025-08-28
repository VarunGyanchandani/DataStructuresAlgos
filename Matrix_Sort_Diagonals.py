from typing import List


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        result = [[0] * n for _ in range(n)]

        for d in range(-(n - 1), n):
            values = []
            positions = []
            start_i = max(0, d)
            end_i = min(n - 1, n - 1 + d)
            for i in range(start_i, end_i + 1):
                j = i - d
                values.append(grid[i][j])
                positions.append((i, j))

            if d >= 0:
                values.sort(reverse=True)
            else:
                values.sort()

            for k in range(len(positions)):
                ii, jj = positions[k]
                result[ii][jj] = values[k]

        return result


# Sample input matrix
input_matrix = [
    [10, 2, 30, 4],
    [5, 6, 7, 8],
    [9, 1, 11, 12],
    [13, 14, 15, 3]
]

solution = Solution()
sorted_matrix = solution.sortMatrix(input_matrix)

# Print results
print("Original Matrix:")
for row in input_matrix:
    print(row)

print("\nSorted Matrix (by diagonals):")
for row in sorted_matrix:
    print(row)
