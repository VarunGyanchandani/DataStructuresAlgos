from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculate current area
            width = right - left
            curr_area = min(height[left], height[right]) * width
            max_area = max(max_area, curr_area)

            # Move the pointer of the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


if __name__ == "__main__":
    solution = Solution()

    heights1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print("Heights:", heights1)
    print("Maximum water container area:", solution.maxArea(heights1))  # Expected output: 49

    heights2 = [1, 1]
    print("\nHeights:", heights2)
    print("Maximum water container area:", solution.maxArea(heights2))  # Expected output: 1

    heights3 = [4, 3, 2, 1, 4]
    print("\nHeights:", heights3)
    print("Maximum water container area:", solution.maxArea(heights3))  # Expected output: 16

    heights4 = [1, 2, 1]
    print("\nHeights:", heights4)
    print("Maximum water container area:", solution.maxArea(heights4))  # Expected output: 2
