def countGoodStrings(low: int, high: int, zero: int, one: int) -> int:
    MOD = 10 ** 9 + 7

    # dp[i] represents the number of valid strings of length i
    dp = [0] * (high + 1)

    # Base case - empty string
    dp[0] = 1

    # For each length i, calculate number of valid strings
    for i in range(high):
        # Add zeros
        if i + zero <= high:
            dp[i + zero] = (dp[i + zero] + dp[i]) % MOD

        # Add ones
        if i + one <= high:
            dp[i + one] = (dp[i + one] + dp[i]) % MOD

    # Sum up all valid lengths between low and high
    result = 0
    for i in range(low, high + 1):
        result = (result + dp[i]) % MOD

    return result

print(countGoodStrings(3,3,1,1))