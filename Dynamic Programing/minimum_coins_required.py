def get_min_coins(coins, change):
	dp = [[float("inf") for i in range(change + 1)] for _ in range(len(coins) + 1)]

	for i in range(1, len(coins) + 1):
		dp[i][0] = 0

	dp[0][0] = float("inf")
	for i in range(1, len(coins) + 1):
		for j in range(1, change + 1):

			if coins[i-1] <= j:
					dp[i][j] = min(dp[i][j - coins[i-1]] + 1, dp[i-1][j])

			else:
				dp[i][j] = dp[i-1][j]

	return dp[-1][-1]

get_min_coins([1, 2, 3], 20)
