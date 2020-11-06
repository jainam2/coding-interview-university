def solve(arr, i, j):
	if i >= j:
		return 0

	ans = float("inf")
	for k in range(i, j):
		temp_ans = solve(arr, i, k) + solve(arr, k+1, j) + arr[i-1] * arr[k] * arr[j]

		if temp_ans < ans:
			ans = temp_ans
	return ans

print(solve([10, 30, 5, 60], 1, 3))
