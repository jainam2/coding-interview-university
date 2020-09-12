import random

def quick_sort(array):

	if len(array) <= 1:
		return array
	
	random.shuffle(array)
	
	pivot = array[-1]
	i, j = 0, len(array) - 2

	while i <= j:
		
		while array[i] <= pivot and i <= j:
			i += 1
			
		while array[j] > pivot and i <= j:
			j -= 1
			
		if i <= j:
			array[i], array[j] = array[j], array[i]
			i += 1
			j -= 1


	return quick_sort(array[:i]) + [pivot] +  quick_sort(array[i: -1])
