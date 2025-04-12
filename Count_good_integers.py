from math import factorial
from collections import Counter
from itertools import permutations


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        total_good = 0

        # Precompute factorials up to n.
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i

        # Given a frequency list f (length 10) sum of digits = n.
        # Count number of n-digit numbers with this multiset:
        def count_numbers(f):
            total_perm = fact[n]
            for cnt in f:
                total_perm //= fact[cnt]
            # subtract those with leading zero if any zeros are present.
            if f[0] > 0:
                bad = fact[n - 1]
                # reduce count of 0 by one, then count arrangements of the rest
                for i, cnt in enumerate(f):
                    if i == 0:
                        bad //= fact[cnt - 1]
                    else:
                        bad //= fact[cnt]
            else:
                bad = 0
            return total_perm - bad

        # Check if frequency vector f (list of 10 ints) is palindromic possible.
        def can_form_palindrome(f):
            if n % 2 == 0:
                return all(cnt % 2 == 0 for cnt in f)
            else:
                odd_count = sum(cnt % 2 for cnt in f)
                return odd_count == 1

        # Build the half of the palindrome given frequency vector f.
        def build_half(f):
            half = []
            for d in range(10):
                half.extend([d] * (f[d] // 2))
            return half

        # Given a half array (list of digits) and possibly a middle digit,
        # Try every unique permutation of the half to see if we can form a valid palindrome
        # that is divisible by k.
        def exists_valid_palindrome(half, middle=None):
            if not half and middle is not None:
                # n == 1 case: check the single middle digit.
                if middle != 0 and middle % k == 0:
                    return True
                else:
                    return False
            seen = set()
            for perm in permutations(half):
                if perm in seen:
                    continue
                seen.add(perm)
                # Leading digit must not be zero.
                if perm[0] == 0:
                    continue
                # Build the number as a list of digits.
                if middle is None:
                    full = list(perm) + list(perm)[::-1]
                else:
                    full = list(perm) + [middle] + list(perm)[::-1]
                # Convert list of digits to integer
                num = 0
                for d in full:
                    num = num * 10 + d
                if num % k == 0:
                    return True
            return False

        # Recursively enumerate all frequency distributions f[0..9] that sum to n.
        def dfs(digit, remaining, current):
            nonlocal total_good
            if digit == 9:
                # Only one possibility remains.
                current.append(remaining)
                # current now is a frequency vector of length 10.
                f = current[:]  # copy
                # skip if the multiset represents all zeros (leading 0) because it is not an n-digit number.
                if f[0] == n:
                    current.pop()
                    return
                # Check palindromic possibility.
                if can_form_palindrome(f):
                    # Build the half and, if needed, determine the middle digit.
                    half = build_half(f)
                    middle = None
                    if n % 2 == 1:
                        # find the digit with odd count.
                        for d in range(10):
                            if f[d] % 2 == 1:
                                middle = d
                                break
                    # Now check if there exists any palindromic arrangement (with no leading zero) divisible by k.
                    if exists_valid_palindrome(half, middle):
                        total_good += count_numbers(f)
                current.pop()
                return

            # For current digit, assign count from 0 to remaining.
            for cnt in range(remaining + 1):
                current.append(cnt)
                dfs(digit + 1, remaining - cnt, current)
                current.pop()

        dfs(0, n, [])
        return total_good


# --- Testing on the provided examples ---
if __name__ == '__main__':
    sol = Solution()
    print(sol.countGoodIntegers(3, 5))  # Expected output: 27
    print(sol.countGoodIntegers(1, 4))  # Expected output: 2
    print(sol.countGoodIntegers(5, 6))  # Expected output: 2468
