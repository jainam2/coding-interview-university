def lcs(str1, str2):
	dp = [[0 for i in range(len(str1) + 1)] for i in range(len(str2) + 1)]
	maxi = 0
	for i in range(1, len(str2) + 1):
		for j in range(1, len(str1) + 1):

			if str1[j-1] == str2[i-1]:
				dp[i][j] = dp[i-1][j-1] + 1
				maxi = max(maxi, dp[i][j])
			else:
				dp[i][j] = 0
			print(dp[i][j], end=" ")
		print()
	return maxi

str1 = input()
str2 = input()

print(lcs(str1, str2))   # Iterative approach (Top down)
