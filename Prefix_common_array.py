def prefix_common_array(A, B):
    n = len(A)
    seen_in_A = set()
    seen_in_B = set()
    C = []

    common = set()  # Track numbers that are common in A and B

    for i in range(n):
        # Add current elements of A and B to respective seen sets
        seen_in_A.add(A[i])
        seen_in_B.add(B[i])

        # Update common set
        if A[i] in seen_in_B:
            common.add(A[i])
        if B[i] in seen_in_A:
            common.add(B[i])

        # Count of common elements so far
        C.append(len(common))

    return C


# Example usage
A1 = [1, 3, 2, 4]
B1 = [3, 1, 2, 4]
print(prefix_common_array(A1, B1))  # Output: [0, 2, 3, 4]

A2 = [2, 3, 1]
B2 = [3, 1, 2]
print(prefix_common_array(A2, B2))  # Output: [0, 1, 3]
