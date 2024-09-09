class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createLinkedList(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def generateMatrix(m, n, head):
    # Initialize the matrix with -1
    matrix = [[-1] * n for _ in range(m)]

    # Initialize boundaries
    top, bottom = 0, m - 1
    left, right = 0, n - 1

    # Traverse the linked list and fill the matrix in spiral order
    current = head

    while top <= bottom and left <= right:
        # Fill top row
        for col in range(left, right + 1):
            if current:
                matrix[top][col] = current.val
                current = current.next
        top += 1

        # Fill right column
        for row in range(top, bottom + 1):
            if current:
                matrix[row][right] = current.val
                current = current.next
        right -= 1

        # Fill bottom row
        for col in range(right, left - 1, -1):
            if current:
                matrix[bottom][col] = current.val
                current = current.next
        bottom -= 1

        # Fill left column
        for row in range(bottom, top - 1, -1):
            if current:
                matrix[row][left] = current.val
                current = current.next
        left += 1

    return matrix

# Example usage
print(generateMatrix(1, 4, createLinkedList([0, 1, 2])))
print(generateMatrix(3, 5, createLinkedList([3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0])))
