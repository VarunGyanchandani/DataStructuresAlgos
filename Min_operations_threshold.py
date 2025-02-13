import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Convert the list to a min-heap
        heapq.heapify(nums)

        operations = 0

        while len(nums) > 1 and nums[0] < k:
            # Pop the two smallest elements
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)

            # Compute the new element
            new_element = min(x, y) * 2 + max(x, y)

            # Push the new element back into the heap
            heapq.heappush(nums, new_element)

            # Increment the operation count
            operations += 1

        # If there's only one element left and it's less than k, we need one more operation
        if len(nums) == 1 and nums[0] < k:
            operations += 1

        return operations

solution = Solution()
nums = [2, 11, 10, 1, 3]
k = 10
print(solution.minOperations(nums, k))  # Output: 2