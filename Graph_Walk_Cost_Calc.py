class UF:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return
        if self.rank[xr] < self.rank[yr]:
            self.parent[xr] = yr
        elif self.rank[xr] > self.rank[yr]:
            self.parent[yr] = xr
        else:
            self.parent[yr] = xr
            self.rank[xr] += 1

class Solution:
    def minimumCost(self, n: int, edges: list[list[int]], query: list[list[int]]) -> list[int]:
        # Union-find for full graph connectivity.
        uf = UF(n)
        for u, v, w in edges:
            uf.union(u, v)

        # Group edges by component.
        # Use a high initial mask; since weights <= 10^5, we need at most 18 bits.
        full_mask = (1 << 18) - 1  # 262143, i.e. all bits set for numbers up to 10^5.

        # comp_mask: for each component representative, store the AND of all edges in that component.
        comp_mask = {}
        for u, v, w in edges:
            comp = uf.find(u)
            if comp not in comp_mask:
                comp_mask[comp] = full_mask
            comp_mask[comp] &= w

        # For vertices that are isolated (no edge), we leave them out; note s and t in such case are not connected.
        ans = []
        for s, t in query:
            if uf.find(s) != uf.find(t):
                ans.append(-1)
            else:
                comp = uf.find(s)
                # If there were no edges in the component (isolated vertex), then no valid walk exists
                # since query guarantees s != t.
                ans.append(comp_mask.get(comp, -1))
        return ans

# Example Usage:
n = 6
edges = [[0, 1, 3], [1, 2, 5], [3, 4, 2], [4, 5, 4]]
query = [[0, 2], [0, 3], [3, 5], [0,4], [0,5], [5,2]]

solution = Solution()
result = solution.minimumCost(n, edges, query)
print(result)
