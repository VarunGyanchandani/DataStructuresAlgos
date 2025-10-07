import heapq
from typing import List
from collections import defaultdict, deque


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n
        dry_days = []  # min-heap of available dry days
        lake_last_rain = {}  # lake -> last rain day
        urgent = []  # min-heap of (next_rain_day, lake) pairs

        # First pass: record all dry days and build urgent queue
        for i in range(n):
            if rains[i] == 0:
                heapq.heappush(dry_days, i)
                ans[i] = 1  # placeholder
            else:
                lake = rains[i]
                if lake in lake_last_rain:
                    # This lake will flood unless we dry it between last rain and now
                    heapq.heappush(urgent, (lake_last_rain[lake], lake))
                lake_last_rain[lake] = i

        # Reset for second pass
        lake_last_rain = {}

        for i in range(n):
            if rains[i] > 0:
                lake = rains[i]
                if lake in lake_last_rain:
                    # Need to dry this lake using a dry day between last_rain and current day
                    last_rain_day = lake_last_rain[lake]

                    # Find the earliest dry day after last_rain_day
                    if not dry_days or dry_days[0] >= i:
                        return []

                    # Binary search in dry_days to find first dry day > last_rain_day
                    temp = []
                    found = False
                    while dry_days and dry_days[0] < i:
                        dry_day = heapq.heappop(dry_days)
                        if dry_day > last_rain_day and not found:
                            ans[dry_day] = lake
                            found = True
                        else:
                            temp.append(dry_day)

                    # Put back unused dry days
                    for day in temp:
                        heapq.heappush(dry_days, day)

                    if not found:
                        return []

                lake_last_rain[lake] = i

        return ans


# Test harness to demonstrate usage
def test_avoid_flood():
    solution = Solution()

    # Test case 1: Example from LeetCode
    rains1 = [1, 2, 0, 0, 2, 1]
    print(f"Input: rains = {rains1}")
    result1 = solution.avoidFlood(rains1)
    print(f"Output: {result1}")

    # Test case 2: Impossible to avoid flooding
    rains2 = [1, 2, 0, 2, 1]
    print(f"\nInput: rains = {rains2}")
    result2 = solution.avoidFlood(rains2)
    print(f"Output: {result2}")

    # Test case 3: More complex case with multiple lakes
    rains3 = [1, 0, 2, 0, 2, 1, 0, 3, 0, 1]
    print(f"\nInput: rains = {rains3}")
    result3 = solution.avoidFlood(rains3)
    print(f"Output: {result3}")


if __name__ == "__main__":
    test_avoid_flood()