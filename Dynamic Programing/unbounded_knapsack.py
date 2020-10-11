# Same problem as Rod Cutting problem no changes.

def get_max(weight, value, capacity):
	
	dp = [[0 for j in range(capacity + 1)] for i in range(len(value) + 1)]

	for  i in range(1, len(value ) + 1):
		for j in range(1, capacity + 1):
		
			if weight[i-1] <= j:
				dp[i][j] = max(value[i - 1] + dp[i][j - weight[i-1]], dp[i-1][j])

			else:
				dp[i][j] = dp[i-1][j]

			print(dp[i][j], end=" ")

		print()

get_max([1, 3, 4, 5], [1, 3, 7, 5], 10)
