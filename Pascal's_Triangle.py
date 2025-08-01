from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            if i == 0:
                row = [1]
            else:
                prev_row = result[-1]
                row = [1] + [prev_row[j] + prev_row[j+1] for j in range(len(prev_row)-1)] + [1]
            result.append(row)
        return result

# Example usage
sol = Solution()
triangle = sol.generate(5)

for row in triangle:
    print(row)
    
triangle = sol.generate(7)

for row in triangle:
    print(row)
