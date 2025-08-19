from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        total_count = 0
        i = 0

        while i < len(nums):
            if nums[i] == 0:
                # Count consecutive zeros starting from index i
                consecutive_zeros = 0
                while i < len(nums) and nums[i] == 0:
                    consecutive_zeros += 1
                    i += 1

                total_count += consecutive_zeros * (consecutive_zeros + 1) // 2
            else:
                i += 1

        return total_count


# Alternative more concise solution
class SolutionConcise:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        """
        More concise version using running count approach.
        """
        result = 0
        current_zeros = 0

        for num in nums:
            if num == 0:
                current_zeros += 1
                result += current_zeros  # Add current sequence length
            else:
                current_zeros = 0

        return result


# Test cases
def test_solutions():
    sol = Solution()
    sol_concise = SolutionConcise()

    # Test case 1
    nums1 = [1, 3, 0, 0, 2, 0, 0, 4]
    expected1 = 6
    assert sol.zeroFilledSubarray(nums1) == expected1
    assert sol_concise.zeroFilledSubarray(nums1) == expected1
    print(f"Test 1 passed: {nums1} -> {expected1}")

    # Test case 2
    nums2 = [0, 0, 0, 2, 0, 0]
    expected2 = 9
    assert sol.zeroFilledSubarray(nums2) == expected2
    assert sol_concise.zeroFilledSubarray(nums2) == expected2
    print(f"Test 2 passed: {nums2} -> {expected2}")

    # Test case 3
    nums3 = [2, 10, 2019]
    expected3 = 0
    assert sol.zeroFilledSubarray(nums3) == expected3
    assert sol_concise.zeroFilledSubarray(nums3) == expected3
    print(f"Test 3 passed: {nums3} -> {expected3}")

    # Additional test cases
    nums4 = [0]
    expected4 = 1
    assert sol.zeroFilledSubarray(nums4) == expected4
    print(f"Test 4 passed: {nums4} -> {expected4}")

    nums5 = [0, 0, 0, 0]
    expected5 = 10  # 4*5//2 = 10
    assert sol.zeroFilledSubarray(nums5) == expected5
    print(f"Test 5 passed: {nums5} -> {expected5}")

    print("All tests passed!")

test_solutions()