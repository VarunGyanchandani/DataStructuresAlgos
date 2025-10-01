class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        if numBottles < numExchange:
            return numBottles

        return numBottles + (numBottles - 1) // (numExchange - 1)


solution = Solution()

numBottles = 9
numExchange = 3
result = solution.numWaterBottles(numBottles, numExchange)
print(f"Total bottles you can drink with {numBottles} bottles and {numExchange} exchange rate: {result}")

numBottles = 15
numExchange = 4
result = solution.numWaterBottles(numBottles, numExchange)
print(f"Total bottles you can drink with {numBottles} bottles and {numExchange} exchange rate: {result}")

numBottles = 5
numExchange = 2
result = solution.numWaterBottles(numBottles, numExchange)
print(f"Total bottles you can drink with {numBottles} bottles and {numExchange} exchange rate: {result}")

numBottles = 2
numExchange = 3
result = solution.numWaterBottles(numBottles, numExchange)
print(f"Total bottles you can drink with {numBottles} bottles and {numExchange} exchange rate: {result}")
