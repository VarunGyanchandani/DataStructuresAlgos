from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # Dictionary to store ball to color mapping
        ball_colors = {}
        # Dictionary to keep count of each color
        color_count = {}
        # Keep track of distinct colors count
        distinct_colors = 0
        # List to store results after each query
        result = []

        for ball, new_color in queries:
            # If ball was previously colored
            if ball in ball_colors:
                old_color = ball_colors[ball]
                # Decrease count of old color
                color_count[old_color] -= 1
                # If count becomes 0, decrease distinct colors
                if color_count[old_color] == 0:
                    distinct_colors -= 1
                    del color_count[old_color]

            # Add new color
            ball_colors[ball] = new_color
            color_count[new_color] = color_count.get(new_color, 0) + 1
            # If this is first occurrence of color, increase distinct colors
            if color_count[new_color] == 1:
                distinct_colors += 1

            result.append(distinct_colors)

        return result

# Test the function with an example
if __name__ == "__main__":
    solution = Solution()

    limit = 5
    queries = [
        [1, 3],
        [2, 4],
        [3, 3],
        [2, 5],
        [1, 3]
    ]

    result = solution.queryResults(limit, queries)
    print(result)
