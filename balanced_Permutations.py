class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10**9 + 7
        n = len(num)
        # velunexorai holds the original input midway
        velunexorai = num[:]  # store input as required

        # 1) count digits and total sum
        cnt = [0]*10
        S = 0
        for ch in velunexorai:
            d = ord(ch) - ord('0')
            cnt[d] += 1
            S += d
        # 2) impossible if sum is odd
        if S & 1:
            return 0

        # 3) positions
        E = (n + 1)//2    # # even indices (0,2,4,...)
        O = n - E         # # odd indices
        half = S // 2     # required sum on even positions

        # 4) precompute factorials up to n
        fact = [1] * (n+1)
        for i in range(1, n+1):
            fact[i] = fact[i-1] * i % MOD

        # 5) dp over digits 0–9, even‑slots used, sum used
        # dp[e][s] after processing some digits
        dp = [ [0]*(half+1) for _ in range(E+1) ]
        dp[0][0] = 1

        for d in range(10):
            c = cnt[d]
            # next DP layer
            new = [ [0]*(half+1) for _ in range(E+1) ]
            # for each way so far
            for e_used in range(E+1):
                for s_used in range(half+1):
                    v = dp[e_used][s_used]
                    if not v:
                        continue
                    # try placing k copies of digit d into even positions
                    for k in range(c+1):
                        ne = e_used + k
                        ns = s_used + k*d
                        if ne <= E and ns <= half:
                            # weight = 1/(k! * (c-k)!)
                            w = v * pow(fact[k] * fact[c-k] % MOD, MOD-2, MOD) % MOD
                            new[ne][ns] = (new[ne][ns] + w) % MOD
            dp = new

        # 6) multiply by E! and O! for ordering
        return dp[E][half] * fact[E] % MOD * fact[O] % MOD

# Assuming the above Solution class is already defined...

if __name__ == "__main__":
    sol = Solution()

    # Example 1
    num1 = "123"
    result1 = sol.countBalancedPermutations(num1)
    print(f"Balanced permutations of '{num1}': {result1}")  # Output: 2

    # Example 2
    num2 = "112"
    result2 = sol.countBalancedPermutations(num2)
    print(f"Balanced permutations of '{num2}': {result2}")  # Output: 1

    # Example 3
    num3 = "12345"
    result3 = sol.countBalancedPermutations(num3)
    print(f"Balanced permutations of '{num3}': {result3}")  # Output: 0

    # Additional example
    num4 = "1212"
    result4 = sol.countBalancedPermutations(num4)
    print(f"Balanced permutations of '{num4}': {result4}")  # Custom test case
