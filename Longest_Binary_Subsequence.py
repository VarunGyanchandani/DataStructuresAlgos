class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        zero_count = s.count('0')

        ones_value = 0
        ones_count = 0
        power = 1  # 2^0

        # Iterate through the string from right to left
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '1':
                # Check if adding this '1' bit keeps us <= k
                if ones_value + power <= k:
                    ones_value += power
                    ones_count += 1

            power *= 2

            if power > k:
                break

        return zero_count + ones_count

sol = Solution()
s = "1001010"
k = 5
print(sol.longestSubsequence(s, k))  