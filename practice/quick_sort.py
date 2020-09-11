import random

def quick_sort(array):

	if len(array) <= 1:
		return array

	pivot = random.choice(array)
	hi, lo, eq = [], [], []

	for i in array:
		if i < pivot:
			lo.append(i)
		elif i > pivot:
			hi.append(i)
		else:
			eq.append(i)

	return quick_sort(lo) + eq + quick_sort(hi)
