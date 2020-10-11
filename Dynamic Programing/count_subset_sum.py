def get_min(arr, _sum):
	
	dp = [[0 for j in range(_sum + 1)] for i in range(len(arr) + 1)]

	for  i in range(0, len(arr) + 1):
		for j in range(0, _sum + 1):
	
			if j == 0:
				dp[i][j] = 1
			elif i == 0:
				dp[i][j] = 0

			else:
				if arr[i-1] <= j:
					dp[i][j] = dp[i - 1][j - arr[i-1]] + dp[i-1][j]
				else:
					dp[i][j] = dp[i-1][j]

			print(dp[i][j], end=" ")

		print()

	return dp[-1][-1]

print(get_min([2, 3, 5, 8, 10], 10))
