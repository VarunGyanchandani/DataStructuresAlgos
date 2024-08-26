class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


def postorder(root):
    def traverse(node):
        if node is None:
            return []

        result = []
        # Visit all children
        for child in node.children:
            result.extend(traverse(child))
        # Visit the node itself
        result.append(node.val)

        return result

    return traverse(root)

# Example 1
root1 = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
print(postorder(root1))

# Example 2
root2 = Node(1, [
    Node(2),
    Node(3, [
        Node(6),
        Node(7, [
            Node(14)
        ])
    ]),
    Node(4, [
        Node(12),
        Node(8, [
            Node(9),
            Node(10)
        ])
    ]),
    Node(5, [
        Node(13)
    ])
])
print(postorder(root2))