class Solution:
    def countWays(self, digits):
        # Handle edge cases
        if not digits or digits[0] == '0':
            return 0

        n = len(digits)

        # Initialize dp array
        # dp[i] represents the number of ways to decode the first i characters
        dp = [0] * (n + 1)
        dp[0] = 1  # Empty string can be decoded in 1 way
        dp[1] = 1  # First character can be decoded in 1 way if it's not '0'

        for i in range(2, n + 1):
            # Current digit (one digit)
            if digits[i - 1] != '0':
                dp[i] += dp[i - 1]

            # Current and previous digit (two digits)
            two_digits = int(digits[i - 2:i])
            if 10 <= two_digits <= 26:
                dp[i] += dp[i - 2]

        return dp[n]


# Create an instance of the Solution class
decoder = Solution()

# Test with example inputs
example1 = "123"
result1 = decoder.countWays(example1)
print(f"Input: {example1}")
print(f"Output: {result1}")
print(f"Explanation: '123' can be decoded as 'ABC'(1,2,3), 'LC'(12,3) and 'AW'(1,23).")

example2 = "90"
result2 = decoder.countWays(example2)
print(f"\nInput: {example2}")
print(f"Output: {result2}")
print(f"Explanation: '90' cannot be decoded, as '0' is an invalid character on its own.")

example3 = "05"
result3 = decoder.countWays(example3)
print(f"\nInput: {example3}")
print(f"Output: {result3}")
print(f"Explanation: '05' cannot be mapped because of the leading zero.")
