from typing import List

class Solution:

    def getNoZeroIntegers(self, n: int) -> List[int]:

        for a in range(1, n):
            b = n - a
            if '0' not in str(a) and '0' not in str(b):
                return [a, b]


if __name__ == "__main__":
    solution = Solution()

    n = 11
    result = solution.getNoZeroIntegers(n)
    print(f"No-zero integers that sum to {n}: {result}")

    n = 101
    result = solution.getNoZeroIntegers(n)
    print(f"No-zero integers that sum to {n}: {result}")

    n = 10000
    result = solution.getNoZeroIntegers(n)
    print(f"No-zero integers that sum to {n}: {result}")
