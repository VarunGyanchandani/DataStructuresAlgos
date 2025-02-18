class Solution:
    def smallestNumber(self, pattern: str) -> str:
        # The result array
        n = len(pattern)
        result = []
        # A stack to store numbers
        stack = []

        # We'll use digits from 1 to n + 1
        for i in range(n + 1):
            stack.append(i + 1)

            # If we reach the end or find an 'I', we pop from the stack
            if i == n or pattern[i] == 'I':
                while stack:
                    result.append(str(stack.pop()))

        return ''.join(result)

pattern = "IIIDIDDD"
sol = Solution()
print(sol.smallestNumber(pattern))  # Output: "123549876"

pattern = "DDD"
sol = Solution()
print(sol.smallestNumber(pattern))  # Output: "4321"
