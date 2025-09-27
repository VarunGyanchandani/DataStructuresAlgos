from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area = 0
        n = len(points)

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    # Using Shoelace formula for triangle area
                    area = 0.5 * abs(
                        points[i][0] * (points[j][1] - points[k][1]) +
                        points[j][0] * (points[k][1] - points[i][1]) +
                        points[k][0] * (points[i][1] - points[j][1])
                    )
                    max_area = max(max_area, area)

        return max_area


# Example usage
if __name__ == "__main__":
    # Sample coordinates: think of these as landmarks on a map or points drawn on a canvas
    points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]

    sol = Solution()
    largest_area = sol.largestTriangleArea(points)

    print(f"The largest triangle area from the given points is: {largest_area:.2f}")
