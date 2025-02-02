class Solution:
    def check(self, nums):
        # Count the number of positions where the array is not sorted
        n = len(nums)
        rotations = 0

        # Compare each adjacent pair including the wrap-around
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                rotations += 1

            # If we find more than one rotation point, it's not a rotated sorted array
            if rotations > 1:
                return False

        return True


# Test cases
def test_solution():
    sol = Solution()

    # Test case 1: [3,4,5,1,2] -> True
    assert sol.check([3, 4, 5, 1, 2]) == True

    # Test case 2: [2,1,3,4] -> False
    assert sol.check([2, 1, 3, 4]) == False

    # Test case 3: [1,2,3] -> True
    assert sol.check([1, 2, 3]) == True

    # Additional test cases
    assert sol.check([1, 1, 1]) == True  # All equal elements
    assert sol.check([2, 1]) == True  # Two elements
    assert sol.check([1]) == True  # Single element
    assert sol.check([6, 10, 6]) == False  # Not possible through rotation