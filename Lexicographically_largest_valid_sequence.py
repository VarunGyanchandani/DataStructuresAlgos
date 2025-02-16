from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        size = 2 * n - 1
        result = [0] * size
        used = set()

        def backtrack(index: int) -> bool:
            if index == size:
                return True  # Successfully filled the sequence

            if result[index] != 0:  # Skip already filled positions
                return backtrack(index + 1)

            for num in range(n, 0, -1):  # Try placing the largest number first
                if num in used:
                    continue

                if num == 1:  # 1 appears only once
                    result[index] = 1
                    used.add(1)
                    if backtrack(index + 1):
                        return True
                    result[index] = 0
                    used.remove(1)

                else:
                    if index + num < size and result[index + num] == 0:
                        result[index] = result[index + num] = num
                        used.add(num)

                        if backtrack(index + 1):
                            return True

                        result[index] = result[index + num] = 0
                        used.remove(num)

            return False

        backtrack(0)
        return result

n = 3
solution = Solution()
result = solution.constructDistancedSequence(n)
print(f"For n = {n}, the distanced sequence is: {result}")

n = 4
result = solution.constructDistancedSequence(n)
print(f"For n = {n}, the distanced sequence is: {result}")

n=5
result = solution.constructDistancedSequence(n)
print(f"For n = {n}, the distanced sequence is: {result}")

n=10
result = solution.constructDistancedSequence(n)
print(f"For n = {n}, the distanced sequence is: {result}")