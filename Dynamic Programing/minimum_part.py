def solve(s, i, j):
	if i >= j or s[i: j+1] == s[i: j+1][::-1]:
		return 0

	ans = float("inf")
	for k in range(i, j):
		ans =  min(ans, 1 + solve(s, i, k) + solve(s, k+1, j))
	return ans

s = input()
print(solve(s, 0, len(s)-1))
