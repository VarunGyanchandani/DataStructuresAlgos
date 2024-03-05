import sys

def findMaximumProduct(A):
    # base case
    if len(A) < 2:
        return

    max_product = -sys.maxsize
    max_i = max_j = -1

    # consider every pair of elements
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            # update the maximum product if required
            if max_product < A[i] * A[j]:
                max_product = A[i] * A[j]
                (max_i, max_j) = (i, j)

    print("Pair is", (A[max_i], A[max_j]))


if __name__ == '__main__':
    A = [-10, -3, 5, 6, -2, 8, 20]
    findMaximumProduct(A)