def minOperations(boxes: str) -> list[int]:
    n = len(boxes)
    answer = [0] * n

    # Left-to-right pass
    balls = 0
    operations = 0
    for i in range(n):
        answer[i] += operations
        balls += int(boxes[i])
        operations += balls

    # Right-to-left pass
    balls = 0
    operations = 0
    for i in range(n - 1, -1, -1):
        answer[i] += operations
        balls += int(boxes[i])
        operations += balls

    return answer

# Example usage:
boxes1 = "110"
boxes2 = "001011"
print(minOperations(boxes1))  # Output: [1, 1, 3]
print(minOperations(boxes2))  # Output: [11, 8, 5, 4, 3, 4]
