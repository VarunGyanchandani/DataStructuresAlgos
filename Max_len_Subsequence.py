from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:

        n = len(nums)
        max_length = 0

        # Try each possible remainder for consecutive pair sums
        for remainder in range(k):
            # dp[last_mod] = maximum length of valid subsequence ending with element ≡ last_mod (mod k)
            dp = [0] * k

            for num in nums:
                current_mod = num % k
                best_length = 1  # At minimum, we can start a new subsequence with this element

                # Check what previous element we need to achieve the target remainder
                # If current element is 'c' and we want (prev + c) % k == remainder
                # Then prev % k == (remainder - c) % k
                needed_prev_mod = (remainder - current_mod) % k

                if dp[needed_prev_mod] > 0:
                    best_length = max(best_length, dp[needed_prev_mod] + 1)

                dp[current_mod] = max(dp[current_mod], best_length)

            max_length = max(max_length, max(dp))

        return max_length


# Practical implementation and example usage
def demonstrate_solution():
    """Demonstrate the solution with examples and explanations."""
    solution = Solution()

    # Test cases from the problem
    test_cases = [
        {
            "nums": [1, 2, 3, 4, 5],
            "k": 2,
            "expected": 5,
            "description": "All consecutive pairs sum to odd numbers (1 mod 2)"
        },
        {
            "nums": [1, 4, 2, 3, 1, 4],
            "k": 3,
            "expected": 4,
            "description": "Subsequence [1,4,1,4] has pairs summing to 5≡2 (mod 3)"
        },
        {
            "nums": [1, 2, 1, 2, 1],
            "k": 2,
            "expected": 5,
            "description": "Alternating 1,2 pattern gives pairs summing to 3≡1 (mod 2)"
        },
        {
            "nums": [2, 4, 6, 8],
            "k": 3,
            "expected": 2,
            "description": "No long valid subsequence possible"
        }
    ]

    print("=== Longest Valid Subsequence Solutions ===\n")

    for i, test in enumerate(test_cases, 1):
        result = solution.maximumLength(test["nums"], test["k"])

        print(f"Test Case {i}:")
        print(f"  Input: nums = {test['nums']}, k = {test['k']}")
        print(f"  Expected: {test['expected']}")
        print(f"  Got: {result}")
        print(f"  Status: {'✓ PASS' if result == test['expected'] else '✗ FAIL'}")
        print(f"  Description: {test['description']}")
        print()


def analyze_subsequence(nums, k, subsequence_indices):
    """Helper function to analyze a specific subsequence."""
    subseq = [nums[i] for i in subsequence_indices]
    print(f"Subsequence: {subseq}")
    print(f"Indices: {subsequence_indices}")

    if len(subseq) < 2:
        print("Too short to analyze pairs")
        return

    remainders = []
    for i in range(len(subseq) - 1):
        pair_sum = subseq[i] + subseq[i + 1]
        remainder = pair_sum % k
        remainders.append(remainder)
        print(f"  Pair ({subseq[i]}, {subseq[i + 1]}): sum = {pair_sum}, remainder = {remainder}")

    is_valid = len(set(remainders)) == 1
    print(f"Valid subsequence: {is_valid}")
    if is_valid:
        print(f"All pairs have remainder: {remainders[0]}")

    return is_valid


def interactive_example():
    """Interactive example to understand the algorithm better."""
    print("=== Interactive Example ===")

    # Example: nums = [1, 4, 2, 3, 1, 4], k = 3
    nums = [1, 4, 2, 3, 1, 4]
    k = 3

    print(f"Array: {nums}")
    print(f"k = {k}")
    print(f"Elements mod k: {[x % k for x in nums]}")
    print()

    # Show the optimal subsequence
    print("Analyzing optimal subsequence [1, 4, 1, 4] (indices 0, 1, 4, 5):")
    analyze_subsequence(nums, k, [0, 1, 4, 5])
    print()

    # Show why other subsequences don't work as well
    print("Trying a different subsequence [1, 2, 3] (indices 0, 2, 3):")
    analyze_subsequence(nums, k, [0, 2, 3])
    print()

    # Show the algorithm in action
    solution = Solution()
    result = solution.maximumLength(nums, k)
    print(f"Maximum length found: {result}")


if __name__ == "__main__":
    demonstrate_solution()
    print("\n" + "=" * 50 + "\n")
    interactive_example()