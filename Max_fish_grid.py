from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        # Get the grid dimensions
        m, n = len(grid), len(grid[0])

        # Directions for moving up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Visited set to track visited water cells
        visited = [[False] * n for _ in range(m)]

        # DFS function to explore connected water cells and calculate the total fish in that region
        def dfs(r, c):
            # Stack for iterative DFS
            stack = [(r, c)]
            total_fish = 0
            while stack:
                x, y = stack.pop()
                if visited[x][y]:
                    continue
                visited[x][y] = True
                total_fish += grid[x][y]
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] > 0:
                        stack.append((nx, ny))
            return total_fish

        # Variable to keep track of the maximum fish caught
        max_fish = 0

        # Iterate over all the cells in the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and not visited[i][j]:
                    # Start DFS if the cell is a water cell and hasn't been visited
                    max_fish = max(max_fish, dfs(i, j))

        return max_fish

# Example grid
grid = [
    [0, 2, 3, 0],
    [1, 0, 4, 5],
    [6, 0, 0, 1],
    [0, 0, 0, 7]
]

# Create a Solution object
solution = Solution()

# Call the findMaxFish method with the grid
result = solution.findMaxFish(grid)

# Output the result
print(f"The maximum number of fish that can be caught is: {result}")