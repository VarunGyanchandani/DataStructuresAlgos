from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.values = set()  # Store all valid values in a set for O(1) lookup

        def recover(node: TreeNode, val: int) -> None:
            if not node:
                return

            # Update current node's value
            node.val = val
            self.values.add(val)

            # Recursively recover left and right children
            # Left child = 2 * x + 1
            # Right child = 2 * x + 2
            recover(node.left, 2 * val + 1)
            recover(node.right, 2 * val + 2)

        # Start recovery from root with value 0
        if root:  # Check if root is not None before calling recover.
            recover(root, 0)

    def find(self, target: int) -> bool:
        return target in self.values


# Example Usage 1:
# Construct a TreeNode.  Note that the "hidden" values are not explicitly set here.
# The recover function in FindElements will calculate and set them.
root = TreeNode(-1, TreeNode(-1, TreeNode(-1)), TreeNode(-1))
findElements = FindElements(root)
print(findElements.find(1))  # Output: True
print(findElements.find(2))  # Output: True
print(findElements.find(3))  # Output: False

# Example Usage 2: Empty Tree
root2 = None
findElements2 = FindElements(root2)
print(findElements2.find(1))  # Output: False
print(findElements2.find(0))  # Output: False

# Example Usage 3: Single Node
root3 = TreeNode(-1)
findElements3 = FindElements(root3)
print(findElements3.find(0))  # Output: True
print(findElements3.find(1))  # Output: False

# Example Usage 4: More complex tree.
root4 = TreeNode(-1)
root4.left = TreeNode(-1)
root4.right = TreeNode(-1)
root4.left.left = TreeNode(-1)
root4.left.right = TreeNode(-1)
root4.right.left = TreeNode(-1)
root4.right.right = TreeNode(-1)

findElements4 = FindElements(root4)
print(findElements4.find(0))  # Output: True
print(findElements4.find(1))  # Output: True
print(findElements4.find(2))  # Output: True
print(findElements4.find(3))  # Output: True
print(findElements4.find(4))  # Output: True
print(findElements4.find(5))  # Output: True
print(findElements4.find(6))  # Output: True
print(findElements4.find(7))  # Output: False