class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10 ** 9 + 7

        # dp[i] = number of people who discovered the secret on day i
        dp = [0] * (n + 1)
        dp[1] = 1  # One person discovers the secret on day 1

        for day in range(2, n + 1):
            # Calculate how many people are sharing the secret on this day
            # People share from day (discovery + delay) to day (discovery + forget - 1)
            sharing = 0
            for discover_day in range(1, day):
                start_sharing = discover_day + delay
                stop_knowing = discover_day + forget

                # If this group of people is in their sharing window
                if start_sharing <= day < stop_knowing:
                    sharing = (sharing + dp[discover_day]) % MOD

            dp[day] = sharing

        # Count total people who know the secret on day n
        # (haven't forgotten yet)
        total = 0
        for discover_day in range(1, n + 1):
            forget_day = discover_day + forget
            if forget_day > n:  # They haven't forgotten by day n
                total = (total + dp[discover_day]) % MOD

        return total


def run_tests():
    solution = Solution()

    # Test case 1: Basic case
    n, delay, forget = 6, 2, 4
    result = solution.peopleAwareOfSecret(n, delay, forget)
    print(f"Test 1: n={n}, delay={delay}, forget={forget}")
    print(f"Result: {result} people know the secret on day {n}")
    print(f"Expected: 5\n")

    # Test case 2: Longer period
    n, delay, forget = 4, 1, 3
    result = solution.peopleAwareOfSecret(n, delay, forget)
    print(f"Test 2: n={n}, delay={delay}, forget={forget}")
    print(f"Result: {result} people know the secret on day {n}")
    print(f"Expected: 3\n")

    # Test case 3: Single day
    n, delay, forget = 1, 1, 1
    result = solution.peopleAwareOfSecret(n, delay, forget)
    print(f"Test 3: n={n}, delay={delay}, forget={forget}")
    print(f"Result: {result} people know the secret on day {n}")
    print(f"Expected: 1\n")

    # Test case 4: Larger numbers
    n, delay, forget = 10, 2, 5
    result = solution.peopleAwareOfSecret(n, delay, forget)
    print(f"Test 4: n={n}, delay={delay}, forget={forget}")
    print(f"Result: {result} people know the secret on day {n}")
    print(f"Expected: 19\n")


if __name__ == "__main__":
    print("Running Secret Sharing Simulation Tests")
    print("======================================")
    run_tests()