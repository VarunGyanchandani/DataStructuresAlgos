from collections import deque
from typing import List


def minimumDiameterAfterMerge(edges1: List[List[int]], edges2: List[List[int]]) -> int:
    def get_tree_properties(edges):
        """Get the diameter and center of a tree."""
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(start):
            """Perform BFS and return farthest node and its distance."""
            q = deque([(start, 0)])
            visited = {start}
            farthest_node, max_dist = start, 0
            while q:
                u, dist = q.popleft()
                if dist > max_dist:
                    max_dist = dist
                    farthest_node = u
                for v in adj[u]:
                    if v not in visited:
                        visited.add(v)
                        q.append((v, dist + 1))
            return farthest_node, max_dist

        # Find one end of the diameter
        node1, _ = bfs(0)
        # Find the other end and the diameter
        node2, diameter = bfs(node1)
        # Find the radius (midpoint)
        path = []

        def find_path(u, target, parent):
            if u == target:
                path.append(u)
                return True
            for v in adj[u]:
                if v != parent and find_path(v, target, u):
                    path.append(u)
                    return True
            return False

        find_path(node1, node2, -1)
        radius_nodes = [path[len(path) // 2]]
        if len(path) % 2 == 0:
            radius_nodes.append(path[len(path) // 2 - 1])
        return diameter, radius_nodes

    # Get properties of both trees
    diameter1, centers1 = get_tree_properties(edges1)
    diameter2, centers2 = get_tree_properties(edges2)

    # Merge and calculate the minimum diameter
    min_diameter = float('inf')
    for c1 in centers1:
        for c2 in centers2:
            # Adding an edge between `c1` and `c2`
            merged_diameter = max(diameter1, diameter2, (diameter1 + 1) // 2 + (diameter2 + 1) // 2 + 1)
            min_diameter = min(min_diameter, merged_diameter)

    return min_diameter

print(minimumDiameterAfterMerge([[0,1],[0,2],[0,3]],[[0,1]]))