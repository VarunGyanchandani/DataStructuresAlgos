from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0:
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
            i -= 1
        return [1] + digits

sol = Solution()
print(sol.plusOne([1,2,3]))   # Output: [1,2,4]
print(sol.plusOne([4,3,2,1])) # Output: [4,3,2,2]
print(sol.plusOne([9,9]))     # Output: [1,0,0]
print(sol.plusOne([9,9,9]))   # Output: [1,0,0,0]
