def findChampion(n, edges):
    # Step 1: Compute in-degree for all nodes
    in_degree = [0] * n
    for u, v in edges:
        in_degree[v] += 1

    # Step 2: Identify nodes with in-degree 0
    champions = [i for i in range(n) if in_degree[i] == 0]

    # Step 3: Return result based on the number of potential champions
    if len(champions) == 1:
        return champions[0]  # Unique champion
    return -1  # No unique champion

# Example Usage:
n1 = 3
edges1 = [[0, 1], [1, 2]]
print(findChampion(n1, edges1))  # Output: 0

n2 = 4
edges2 = [[0, 2], [1, 3], [1, 2]]
print(findChampion(n2, edges2))  # Output: -1
