# Python Implementation with Examples

from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        """
        Find all k-distant indices in the array.

        Args:
            nums: List of integers
            key: The target value to find
            k: Maximum distance allowed

        Returns:
            List of k-distant indices sorted in increasing order
        """
        # Find all indices where nums[j] == key
        key_indices = []
        for j in range(len(nums)):
            if nums[j] == key:
                key_indices.append(j)

        result = []

        # For each index i, check if it's k-distant
        for i in range(len(nums)):
            # Check if there exists at least one j such that |i - j| <= k and nums[j] == key
            for j in key_indices:
                if abs(i - j) <= k:
                    result.append(i)
                    break  # Found one valid j, no need to check others

        return result


# Example Usage and Practical Implementation
def run_examples():
    solution = Solution()

    print("=== K-Distant Indices Examples ===\n")

    # Example 1: Basic case
    print("Example 1:")
    nums1 = [3, 4, 9, 1, 3, 9, 5]
    key1 = 9
    k1 = 1
    result1 = solution.findKDistantIndices(nums1, key1, k1)
    print(f"Input: nums = {nums1}, key = {key1}, k = {k1}")
    print(f"Output: {result1}")
    print("Explanation: Key 9 is at indices 2 and 5. Indices within distance 1: [1,2,3,4,5,6]\n")

    # Example 2: All elements are the key
    print("Example 2:")
    nums2 = [2, 2, 2, 2, 2]
    key2 = 2
    k2 = 2
    result2 = solution.findKDistantIndices(nums2, key2, k2)
    print(f"Input: nums = {nums2}, key = {key2}, k = {k2}")
    print(f"Output: {result2}")
    print("Explanation: All elements are key 2, so all indices are k-distant.\n")

    # Example 3: Single occurrence
    print("Example 3:")
    nums3 = [1, 2, 3, 4, 5]
    key3 = 3
    k3 = 2
    result3 = solution.findKDistantIndices(nums3, key3, k3)
    print(f"Input: nums = {nums3}, key = {key3}, k = {k3}")
    print(f"Output: {result3}")
    print("Explanation: Key 3 is at index 2. Indices within distance 2: [0,1,2,3,4]\n")

    # Example 4: No k-distant indices
    print("Example 4:")
    nums4 = [1, 2, 3, 4, 5]
    key4 = 3
    k4 = 0
    result4 = solution.findKDistantIndices(nums4, key4, k4)
    print(f"Input: nums = {nums4}, key = {key4}, k = {k4}")
    print(f"Output: {result4}")
    print("Explanation: Only index 2 (where key 3 is located) is within distance 0.\n")

    # Example 5: Multiple scattered occurrences
    print("Example 5:")
    nums5 = [7, 1, 7, 3, 7, 2, 7]
    key5 = 7
    k5 = 1
    result5 = solution.findKDistantIndices(nums5, key5, k5)
    print(f"Input: nums = {nums5}, key = {key5}, k = {k5}")
    print(f"Output: {result5}")
    print("Explanation: Key 7 is at indices 0,2,4,6. All indices are within distance 1 of at least one occurrence.\n")


# Practical Implementation: Process multiple test cases
def process_test_cases(test_cases):
    """
    Process multiple test cases for k-distant indices problem.

    Args:
        test_cases: List of tuples (nums, key, k, expected_output)
    """
    solution = Solution()

    print("=== Processing Test Cases ===\n")

    for i, (nums, key, k, expected) in enumerate(test_cases, 1):
        result = solution.findKDistantIndices(nums, key, k)
        status = "✓ PASS" if result == expected else "✗ FAIL"

        print(f"Test Case {i}: {status}")
        print(f"  Input: nums={nums}, key={key}, k={k}")
        print(f"  Expected: {expected}")
        print(f"  Got: {result}")
        print()


# Interactive function to test custom inputs
def test_custom_input():
    """Allow users to test with custom inputs"""
    solution = Solution()

    print("=== Custom Input Testing ===")
    print("Enter your test case:")

    try:
        nums_input = input("Enter nums (comma-separated): ")
        nums = [int(x.strip()) for x in nums_input.split(',')]

        key = int(input("Enter key: "))
        k = int(input("Enter k: "))

        result = solution.findKDistantIndices(nums, key, k)

        print(f"\nResult: {result}")

        # Show detailed explanation
        key_positions = [i for i, val in enumerate(nums) if val == key]
        print(f"Key {key} found at positions: {key_positions}")

        print("\nDetailed analysis:")
        for i in range(len(nums)):
            distances = [abs(i - pos) for pos in key_positions]
            min_distance = min(distances) if distances else float('inf')
            is_k_distant = min_distance <= k
            print(f"  Index {i}: min distance = {min_distance}, k-distant = {is_k_distant}")

    except ValueError:
        print("Invalid input format. Please enter valid integers.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Run basic examples
    run_examples()

    # # Test cases for validation
    # test_cases = [
    #     ([3, 4, 9, 1, 3, 9, 5], 9, 1, [1, 2, 3, 4, 5, 6]),
    #     ([2, 2, 2, 2, 2], 2, 2, [0, 1, 2, 3, 4]),
    #     ([1, 2, 3, 4, 5], 3, 2, [0, 1, 2, 3, 4]),
    #     ([1, 2, 3, 4, 5], 3, 0, [2]),
    #     ([1], 1, 0, [0]),
    #     ([1, 5, 1, 5, 1], 5, 1, [0, 1, 2, 3, 4])
    # ]
    #
    # process_test_cases(test_cases)

