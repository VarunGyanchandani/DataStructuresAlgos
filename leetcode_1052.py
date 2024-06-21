from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)

        # Calculate satisfied customers when not grumpy
        initial_satisfied = sum(customers[i] for i in range(n) if grumpy[i] == 0)

        # Calculate additional satisfied customers using sliding window
        max_additional = 0
        current_additional = sum(customers[i] for i in range(minutes) if grumpy[i] == 1)
        max_additional = current_additional

        for i in range(minutes, n):
            if grumpy[i - minutes] == 1:
                current_additional -= customers[i - minutes]
            if grumpy[i] == 1:
                current_additional += customers[i]
            max_additional = max(max_additional, current_additional)

        # Total maximum satisfied customers
        return initial_satisfied + max_additional


# Example 1
customers = [1, 0, 1, 2, 1, 1, 7, 5]
grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
minutes = 3
sol = Solution()
print(sol.maxSatisfied(customers, grumpy, minutes))  # Output: 16

# Example 2
customers = [1]
grumpy = [0]
minutes = 1
print(sol.maxSatisfied(customers, grumpy, minutes))  # Output: 1
