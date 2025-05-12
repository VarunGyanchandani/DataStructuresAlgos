import collections  # We'll use Counter for easy frequency counting
from typing import List  # For type hinting


class Solution:

    def findEvenNumbers(self, digits: List[int]) -> List[int]:

        digit_counts = collections.Counter(digits)

        result = []

        for num in range(100, 1000):

            if num % 2 != 0:
                continue  # If odd, skip to the next number in the loop

            d1 = num // 100  # Hundreds digit (312 // 100 = 3)
            d2 = (num // 10) % 10  # Tens digit ((312 // 10) % 10 = 31 % 10 = 1)
            d3 = num % 10  # Units digit (312 % 10 = 2)

            required_counts = collections.Counter([d1, d2, d3])

            can_form_number = True  # Assume we can form it initially

            for d, required_count in required_counts.items():

                if digit_counts[d] < required_count:
                    can_form_number = False
                    break  # No need to check other digits for this number

            if can_form_number:
                result.append(num)

        return result


solver = Solution()
digits1 = [2, 1, 3, 0]
output1 = solver.findEvenNumbers(digits1)
print(f"Input: {digits1}")
print(f"Output: {output1}") # Expected: [102, 120, 130, 132, 210, 230, 302, 310, 312, 320]

digits2 = [2, 2, 8, 8, 2]
output2 = solver.findEvenNumbers(digits2)
print(f"\nInput: {digits2}")
print(f"Output: {output2}") # Expected: [222, 228, 282, 288, 822, 828, 882]

digits3 = [3, 7, 5]
output3 = solver.findEvenNumbers(digits3)
print(f"\nInput: {digits3}")
print(f"Output: {output3}") # Expected: []