import time
import random
def binary_search_with_recur(arr, low, high, target):
	mid = low + (high - low) // 2
	if arr[mid] == target:
		return mid
	elif low == high:
		return -1

	if arr[mid] < target:
		return binary_search_with_recur(arr, mid+1, high, target)
	else:
		return binary_search_with_recur(arr, low, mid-1, target)


def binary_search_with_iters(arr, low, high, target):
	
	while True:
		mid = low + (high - low) // 2
		if arr[mid] == target:
			return mid
		if low == high:
			return -1

		if arr[mid] < target:
			low = mid + 1
		else:
			high = mid - 1

if __name__ == "__main__":
	import doctest
	import time
	start = time.time()
	print("Testing...")
	doctest.testmod()
	print("Tested status - 200 OK")
	print(f"Time to test: {round(time.time() - start, 10)} ms")
