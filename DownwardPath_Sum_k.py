class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def sumK(self, root, k):
        def dfs(node, cumulative_sum):
            if not node:
                return 0

            # Update the current sum
            cumulative_sum += node.data

            # Count the number of valid paths ending at this node
            count = prefix_sums.get(cumulative_sum - k, 0)

            # Update the prefix_sums dictionary
            prefix_sums[cumulative_sum] = prefix_sums.get(cumulative_sum, 0) + 1

            # Recur for left and right subtrees
            count += dfs(node.left, cumulative_sum)
            count += dfs(node.right, cumulative_sum)

            # Backtrack: remove the current sum from the map
            prefix_sums[cumulative_sum] -= 1
            if prefix_sums[cumulative_sum] == 0:
                del prefix_sums[cumulative_sum]

            return count

        prefix_sums = {0: 1}  # To handle cases where a path from root itself sums to k
        return dfs(root, 0)

root = Node(10)
root.left = Node(5)
root.right = Node(-3)
root.left.left = Node(3)
root.left.right = Node(2)
root.right.right = Node(11)
root.left.left.left = Node(3)
root.left.left.right = Node(-2)
root.left.right.right = Node(1)

# Set the value of k
k = 8

# Create an instance of the Solution class
solution = Solution()

# Call sumK method with the root of the tree and k
result = solution.sumK(root, k)

# Print the result
print(f"Number of paths with sum {k}: {result}")
