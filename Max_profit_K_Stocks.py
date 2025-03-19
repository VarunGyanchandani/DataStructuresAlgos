class Solution:
    def maxProfit(self, prices, k):
        n = len(prices)

        # Edge cases
        if n <= 1 or k == 0:
            return 0

        # If k is large enough, we can make as many transactions as we want
        if k >= n // 2:
            # In this case, we can just accumulate all positive price differences
            max_profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    max_profit += prices[i] - prices[i - 1]
            return max_profit

        # dp[i][j] represents maximum profit using at most i transactions up to day j
        dp = [[0 for _ in range(n)] for _ in range(k + 1)]

        for i in range(1, k + 1):
            # Maximum profit we can have if we make ith transaction on day j
            max_diff = -prices[0]

            for j in range(1, n):
                # Two possibilities:
                # 1. Don't make a transaction on day j, carry forward profit from day j-1
                # 2. Sell on day j, which means buying at some previous day and selling now
                dp[i][j] = max(dp[i][j - 1], prices[j] + max_diff)

                # Update max_diff for the next iteration
                max_diff = max(max_diff, dp[i - 1][j] - prices[j])

        return dp[k][n - 1]

    def explain_transactions(self, prices, k):
        """
        Find and explain the optimal transactions for maximum profit
        """
        n = len(prices)

        # Edge cases
        if n <= 1 or k == 0:
            return "No transactions possible", 0

        # If no profit can be made
        if self.maxProfit(prices, k) == 0:
            return "No profitable transactions possible", 0

        # Find optimal transactions using dynamic programming
        # Similar to maxProfit, but we'll track the best buy/sell days
        if k >= n // 2:
            # In this case, we can just accumulate all positive price differences
            transactions = []
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    transactions.append((i - 1, i))

            # Consolidate consecutive buy-sell days
            consolidated = []
            buy_day = transactions[0][0]
            current_sell = transactions[0][1]

            for i in range(1, len(transactions)):
                if transactions[i][0] == current_sell:
                    # Extend current transaction
                    current_sell = transactions[i][1]
                else:
                    # Complete current transaction and start new one
                    consolidated.append((buy_day, current_sell))
                    buy_day = transactions[i][0]
                    current_sell = transactions[i][1]

            consolidated.append((buy_day, current_sell))

            # Calculate profit and format explanation
            total_profit = 0
            explanation = []

            for i, (buy, sell) in enumerate(consolidated):
                profit = prices[sell] - prices[buy]
                total_profit += profit
                explanation.append(
                    f"Transaction {i + 1}: Buy at day {buy} for ${prices[buy]} and sell at day {sell} for ${prices[sell]}. Profit: ${profit}")

            return "\n".join(explanation), total_profit

        # For the more complex case with limited k, we need to backtrack through the DP table
        dp = [[0 for _ in range(n)] for _ in range(k + 1)]

        for i in range(1, k + 1):
            max_diff = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], prices[j] + max_diff)
                max_diff = max(max_diff, dp[i - 1][j] - prices[j])

        # Backtrack to find the transactions
        transactions = []
        i, j = k, n - 1

        while i > 0 and j > 0:
            if dp[i][j] == dp[i][j - 1]:
                # We didn't sell on day j
                j -= 1
            else:
                # We sold on day j, find the buy day
                sell_day = j
                buy_day = j - 1

                # Find the optimal buy day (the day that maximizes profit)
                max_profit = dp[i][sell_day] - (dp[i - 1][buy_day] + prices[buy_day])

                for day in range(j - 2, -1, -1):
                    profit = dp[i][sell_day] - (dp[i - 1][day] + prices[day])
                    if profit > max_profit:
                        max_profit = profit
                        buy_day = day

                transactions.append((buy_day, sell_day))

                # Move to the state before this transaction
                i -= 1
                j = buy_day

        # Reverse transactions to get them in chronological order
        transactions.reverse()

        # Calculate profit and format explanation
        total_profit = 0
        explanation = []

        for i, (buy, sell) in enumerate(transactions):
            profit = prices[sell] - prices[buy]
            total_profit += profit
            explanation.append(
                f"Transaction {i + 1}: Buy at day {buy} for ${prices[buy]} and sell at day {sell} for ${prices[sell]}. Profit: ${profit}")

        return "\n".join(explanation), total_profit


def main():
    # Create solution object
    solution = Solution()

    # Example 1
    prices1 = [10, 22, 5, 80]
    k1 = 2
    profit1 = solution.maxProfit(prices1, k1)
    explanation1, _ = solution.explain_transactions(prices1, k1)

    print("Example 1:")
    print(f"Prices: {prices1}")
    print(f"Maximum transactions allowed: {k1}")
    print(f"Maximum profit: {profit1}")
    print("Explanation:")
    print(explanation1)
    print()

    # Example 2
    prices2 = [20, 580, 420, 900]
    k2 = 3
    profit2 = solution.maxProfit(prices2, k2)
    explanation2, _ = solution.explain_transactions(prices2, k2)

    print("Example 2:")
    print(f"Prices: {prices2}")
    print(f"Maximum transactions allowed: {k2}")
    print(f"Maximum profit: {profit2}")
    print("Explanation:")
    print(explanation2)
    print()

    # Example 3
    prices3 = [100, 90, 80, 50, 25]
    k3 = 1
    profit3 = solution.maxProfit(prices3, k3)
    explanation3, _ = solution.explain_transactions(prices3, k3)

    print("Example 3:")
    print(f"Prices: {prices3}")
    print(f"Maximum transactions allowed: {k3}")
    print(f"Maximum profit: {profit3}")
    print("Explanation:")
    print(explanation3)

    # Additional example
    prices4 = [3, 2, 6, 5, 0, 3]
    k4 = 2
    profit4 = solution.maxProfit(prices4, k4)
    explanation4, _ = solution.explain_transactions(prices4, k4)

    print("\nAdditional Example:")
    print(f"Prices: {prices4}")
    print(f"Maximum transactions allowed: {k4}")
    print(f"Maximum profit: {profit4}")
    print("Explanation:")
    print(explanation4)


if __name__ == "__main__":
    main()