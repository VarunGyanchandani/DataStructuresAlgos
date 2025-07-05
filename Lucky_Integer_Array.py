from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # Count frequency of each number
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        # Find the largest lucky number
        lucky_max = -1
        for num, count in freq.items():
            if num == count:  # Lucky number condition
                lucky_max = max(lucky_max, num)

        return lucky_max


# Example usage:
if __name__ == "__main__":
    ratings = [2, 3, 3, 3, 4, 4, 4, 4, 5, 5]  # Example customer ratings
    solution = Solution()
    lucky_rating = solution.findLucky(ratings)
    print(f"The highest lucky rating is: {lucky_rating}")
