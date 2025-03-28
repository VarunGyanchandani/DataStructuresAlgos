def maxPoints(grid, queries):
    m, n = len(grid), len(grid[0])

    # Helper function to print current state (for demonstration)
    def print_state(visited, points, current_query):
        print(f"\nQuery: {current_query}")
        print("Visited cells:")
        for cell in visited:
            print(f"  {cell}: {grid[cell[0]][cell[1]]}")
        print(f"Current Points: {points}")

    # Tracking function to simulate the process
    def simulate_query(query):
        # Reset for each query
        visited = set([(0, 0)])
        points = 0

        # Directions to move: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Queue to track cells to explore
        queue = [(0, 0)]

        # Track cells that can be explored
        while queue:
            current_cells = queue.copy()
            queue.clear()

            for r, c in current_cells:
                # If current cell value is less than query, we can explore
                if grid[r][c] < query:
                    # Explore adjacent cells
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        # Check if new cell is valid and not visited
                        if (0 <= nr < m and 0 <= nc < n and
                                (nr, nc) not in visited and
                                grid[nr][nc] < query):
                            # Mark as visited and add points
                            visited.add((nr, nc))
                            points += 1
                            queue.append((nr, nc))

                # Print state after exploring each cell
                print_state(visited, points, query)

        return points

    # Process each query
    return [simulate_query(query) for query in queries]


# Test the implementation
grid = [[1, 2, 3], [2, 5, 7], [3, 5, 1]]
queries = [5, 6, 2]

result = maxPoints(grid, queries)
print("\nFinal Result:", result)

# Detailed explanation of each query
print("\nDetailed Explanation:")
for i, (query, points) in enumerate(zip(queries, result)):
    print(f"\nQuery {query}:")
    print(f"Maximum Points: {points}")