from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')

        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum
        return closest_sum


# Example usage:
if __name__ == "__main__":
    prices = [120, 70, 250, 30, 90, 200]
    target_budget = 300

    sol = Solution()
    closest = sol.threeSumClosest(prices, target_budget)

    print(f"The sum of the three item prices closest to ${target_budget} is: ${closest}")
