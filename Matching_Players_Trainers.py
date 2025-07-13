from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i, j = 0, 0
        count = 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1
        return count

solution = Solution()

players = [4, 7, 9]
trainers = [3, 6, 8, 10]

matches = solution.matchPlayersAndTrainers(players, trainers)

print(f"Maximum number of players that can be matched with trainers: {matches}")
