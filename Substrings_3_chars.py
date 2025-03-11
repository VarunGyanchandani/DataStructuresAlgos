class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        result = 0

        # Initialize counts of a, b, c in current window
        count = {'a': 0, 'b': 0, 'c': 0}

        # Initialize left pointer of sliding window
        left = 0

        # Iterate with right pointer
        for right in range(n):
            # Include current character in window
            count[s[right]] += 1

            # Shrink window from left until we don't have all three characters
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                # For each valid window ending at 'right', all possible extensions to the right
                # will also be valid. There are (n - right) such extensions.
                result += n - right

                # Remove leftmost character and move left pointer
                count[s[left]] -= 1
                left += 1

        return result


# Example usage:
solution = Solution()
print(solution.numberOfSubstrings("abcabc"))
