from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Apply operations
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        # Shift all zeros to the end
        result = [num for num in nums if num != 0]
        result.extend([0] * (n - len(result)))

        return result


# Practical implementation with an example
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 2, 1, 1, 0]
    print("Input array:", nums)
    result = solution.applyOperations(nums)
    print("Resulting array after operations and shifting zeros:", result)
