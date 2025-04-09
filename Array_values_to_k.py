from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if any(x < k for x in nums):
            return -1
        if all(x == k for x in nums):
            return 0

        unique_greater_than_k = sorted(list(set(x for x in nums if x > k)), reverse=True)
        operations = 0
        current_nums = list(nums)

        for i, val in enumerate(unique_greater_than_k):
            target = k if i == len(unique_greater_than_k) - 1 else unique_greater_than_k[i + 1]

            is_valid = True
            for x in current_nums:
                if x > target and x != val:
                    is_valid = False
                    break

            if not is_valid:
                return -1

            for j in range(len(current_nums)):
                if current_nums[j] > target:
                    current_nums[j] = target
            operations += 1

        if not all(x == k for x in current_nums):
            return -1

        return operations

# Example Usage
nums = [5, 2, 5, 4, 5]
k = 2
solution = Solution()
result = solution.minOperations(nums, k)
print(f"Minimum operations required: {result}")