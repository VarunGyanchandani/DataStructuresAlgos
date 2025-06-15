class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        max_str = s
        for char in s:
            if char != '9':
                max_str = s.replace(char, '9')
                break

        min_str = s
        if s[0] != '1':
            min_str = s.replace(s[0], '1')
        else:
            for i in range(1, len(s)):
                if s[i] != '0' and s[i] != '1':
                    min_str = s.replace(s[i], '0')
                    break

        return int(max_str) - int(min_str)

sol = Solution()

# Test case
num = 9288

difference = sol.maxDiff(num)

print(f"The maximum difference for {num} is: {difference}")
