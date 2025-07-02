class Solution:
    def myAtoi(self, s: str) -> int:

        i = 0
        sign = 1
        res = 0
        n = len(s)

        # 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # 1. Ignore leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # 2. Determine the sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # 3. Convert the number and handle overflow
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # Check for overflow before appending the new digit
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN

            res = res * 10 + digit
            i += 1

        # 4. Return the final result with the correct sign
        return sign * res


# Example Usage:

solution = Solution()

# Test Cases
test_cases = [
    ("42", 42),
    ("   -42", -42),
    ("4193 with words", 4193),
    ("words and 987", 0),
    ("+123", 123),
    ("-2147483649", -2147483648),
    ("21474836460", 2147483647),
    ("0000000000012345678", 12345678),
    ("", 0),
    ("  +00123abc456", 123),
]

# Running the test cases
for idx, (input_str, expected_output) in enumerate(test_cases):
    result = solution.myAtoi(input_str)
    print(f"Test case {idx + 1}:")
    print(f"Input: '{input_str}'")
    print(f"Expected: {expected_output}, Got: {result}\n")
