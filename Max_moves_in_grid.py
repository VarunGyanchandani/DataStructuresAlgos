def maxMoves(grid):
    m, n = len(grid), len(grid[0])
    memo = [[-1] * n for _ in range(m)]

    def dfs(row, col):
        if memo[row][col] != -1:
            return memo[row][col]

        max_move = 0
        # Check possible moves
        for new_row in [row - 1, row, row + 1]:
            if 0 <= new_row < m and col + 1 < n and grid[new_row][col + 1] > grid[row][col]:
                max_move = max(max_move, 1 + dfs(new_row, col + 1))

        memo[row][col] = max_move
        return max_move

    max_moves = 0
    for i in range(m):
        max_moves = max(max_moves, dfs(i, 0))

    return max_moves

# Example Usage:
grid1 = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
grid2 = [[3,2,4],[2,1,9],[1,1,7]]
print(maxMoves(grid1))  # Output: 3
print(maxMoves(grid2))  # Output: 0
