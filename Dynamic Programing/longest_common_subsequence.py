def lcs(str1, str2):
	dp = [[0 for i in range(len(str1) + 1)] for i in range(len(str2) + 1)]

	for i in range(1, len(str2) + 1):
		for j in range(1, len(str1) + 1):

			if str1[j-1] == str2[i-1]:
				dp[i][j] = dp[i-1][j-1] + 1
			else:
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])
	return dp[-1][-1]

str1 = input()
str2 = input()

print(lcs(str1, str2))   # Iterative approach (Top down)
