class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = amount+1
        dp = [INF] * INF
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        if dp[-1] is not INF:
            return dp[-1]
        return -1
        # [1 2 3 4 2 0 0 0 0 0 0 0]