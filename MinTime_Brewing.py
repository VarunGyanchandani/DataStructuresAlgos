from typing import List


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        m = len(mana)
        cumsum = [0] * (n + 1)
        for i in range(n):
            cumsum[i + 1] = cumsum[i] + skill[i]
        total_sum = cumsum[n]

        start_times = [0] * m
        for j in range(1, m):
            lb = 0
            prev_m = mana[j - 1]
            curr_m = mana[j]
            prev_s = start_times[j - 1]
            for i in range(n):
                temp = prev_s + prev_m * cumsum[i + 1] - cumsum[i] * curr_m
                if temp > lb:
                    lb = temp
            start_times[j] = lb

        max_time = 0
        for j in range(m):
            completion = start_times[j] + mana[j] * total_sum
            if completion > max_time:
                max_time = completion
        return max_time


skill = [3, 2, 5, 4]
mana = [1, 2, 3]

solution = Solution()
min_time = solution.minTime(skill, mana)
print(f"The minimum time required to complete all tasks is: {min_time}")