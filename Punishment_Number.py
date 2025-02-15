class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(num: int, target: int, start: int) -> bool:
            """
            Helper function to check if the square of `num` can be partitioned into contiguous substrings
            that sum up to `num`.
            """
            s = str(num * num)

            def backtrack(index: int, curr_sum: int) -> bool:
                if index == len(s):
                    return curr_sum == target

                val = 0
                for i in range(index, len(s)):
                    val = val * 10 + int(s[i])
                    if curr_sum + val <= target and backtrack(i + 1, curr_sum + val):
                        return True
                return False

            return backtrack(0, 0)

        punishment_sum = 0
        for i in range(1, n + 1):
            if can_partition(i, i, 0):
                punishment_sum += i * i

        return punishment_sum


# Example use case
solution = Solution()
print(solution.punishmentNumber(5))  # Output should be 1
