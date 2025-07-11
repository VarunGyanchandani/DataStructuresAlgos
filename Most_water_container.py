from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            max_area = max(max_area, h * w)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


def main():
    solution = Solution()

    # Example 1
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result = solution.maxArea(height)
    print(f"Max water container area (Example 1): {result}")  # Expected: 49

    # Example 2
    height = [1, 1]
    result = solution.maxArea(height)
    print(f"Max water container area (Example 2): {result}")  # Expected: 1

    # Edge Case: Increasing heights
    height = [1, 2, 3, 4, 5]
    result = solution.maxArea(height)
    print(f"Max water container area (Increasing): {result}")  # Expected: 6

    # Edge Case: All heights are zero
    height = [0, 0, 0, 0]
    result = solution.maxArea(height)
    print(f"Max water container area (All zero): {result}")  # Expected: 0


if __name__ == "__main__":
    main()
