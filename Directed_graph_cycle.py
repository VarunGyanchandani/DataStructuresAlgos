class Solution:
    def isCycle(self, V, edges):
        # Create adjacency list representation of the graph
        adj_list = [[] for _ in range(V)]
        for u, v in edges:
            adj_list[u].append(v)

        # Three states for vertices:
        # 0: not visited
        # 1: being processed (in the current DFS path)
        # 2: completely processed
        visited = [0] * V

        def dfs(node):
            # If the node is in the current DFS path, we found a cycle
            if visited[node] == 1:
                return True

            # If the node has been completely processed in another path, no cycle
            if visited[node] == 2:
                return False

            # Mark the node as being processed
            visited[node] = 1

            # Visit all neighbors
            for neighbor in adj_list[node]:
                if dfs(neighbor):
                    return True

            # Mark the node as completely processed
            visited[node] = 2
            return False

        # Check for cycles starting from each unvisited vertex
        for i in range(V):
            if visited[i] == 0:
                if dfs(i):
                    return True

        return False

# Example 1: Graph with a cycle
V1 = 4
edges1 = [[0, 1], [1, 2], [2, 0], [2, 3]]
solution = Solution()
result1 = solution.isCycle(V1, edges1)
print(f"Does the graph with {V1} vertices and edges {edges1} contain a cycle? {result1}")

# Example 2: Graph without a cycle
V2 = 4
edges2 = [[0, 1], [1, 2], [2, 3]]
result2 = solution.isCycle(V2, edges2)
print(f"Does the graph with {V2} vertices and edges {edges2} contain a cycle? {result2}")
