from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        res: List[int] = []

        # Traverse diagonals
        for k in range(m + n - 1):
            start = max(0, k - (n - 1))
            end = min(m - 1, k)
            diag = []

            for i in range(start, end + 1):
                j = k - i
                diag.append(mat[i][j])

            # Reverse every alternate diagonal
            if k % 2 == 0:
                diag.reverse()

            res.extend(diag)

        return res


if __name__ == "__main__":
    sol = Solution()

    mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Matrix 1:")
    for row in mat1:
        print(row)
    print("Diagonal Order:", sol.findDiagonalOrder(mat1))
    # Expected Output: [1,2,4,7,5,3,6,8,9]

    print("\n-----------------------------------\n")

    mat2 = [[1, 2], [3, 4]]
    print("Matrix 2:")
    for row in mat2:
        print(row)
    print("Diagonal Order:", sol.findDiagonalOrder(mat2))
    # Expected Output: [1,2,3,4]

    print("\n-----------------------------------\n")

    # Larger matrix
    mat3 = [[i + j * 5 for i in range(1, 6)] for j in range(4)]
    print("Matrix 3:")
    for row in mat3:
        print(row)
    print("Diagonal Order:", sol.findDiagonalOrder(mat3))
