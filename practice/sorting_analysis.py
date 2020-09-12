import merge_sort
import quick_sort
import matplotlib.pyplot as plt
import time

n = list(range(10**4, 10**5, 2000))
qs = []
ms = []

for i in n:
	array = list(reversed(range(i)))
	start = time.time()
	arr = merge_sort.merge_sort(array)
	end = time.time()

	ms.append(end-start)

	start = time.time()
	arr = quick_sort.quick_sort(array)
	end = time.time()

	qs.append(end-start)



plt.scatter(n, ms, color="blue", label = "Merge Sort", s=5)
plt.scatter(n, qs, color="red", label = "Quick Sort", s=5)

plt.xlabel("Size")
plt.ylabel("Time")
plt.show()
