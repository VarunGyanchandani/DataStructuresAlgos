import collections

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        # 'left' is the starting index of our sliding window.
        left = 0
        # 'max_fruits' will store the maximum length of a valid subarray found so far.
        max_fruits = 0
        # basket keeps track of the count of fruits in the window
        basket = collections.defaultdict(int)

        # Iterate through each fruit using the right pointer (enumerate for both index and fruit type)
        for right, fruit in enumerate(fruits):
            basket[fruit] += 1

            # If there are more than two types of fruits in the basket, move the left pointer
            while len(basket) > 2:
                # Remove one fruit from the left
                left_fruit = fruits[left]
                basket[left_fruit] -= 1
                if basket[left_fruit] == 0:
                    del basket[left_fruit]
                left += 1  # Shrink the window from the left

            # Calculate the max number of fruits in the current valid window
            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits


fruits = [1, 2, 1, 2, 3]
solution = Solution()
print(solution.totalFruit(fruits))
