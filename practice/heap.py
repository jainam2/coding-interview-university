class heapq:
	
	def __init__(self, arr = []):
		self._heap = arr

	def heapify(self):
		for i in reversed(range(0, self.size() // 2)):
			self._sift_down(i)
		return self._heap

	def right_child(self, index):
		return index * 2 + 2

	def left_child(self, index):
		return index * 2 + 1

	def parent(self, index):
		return (index - 1) // 2

	def _sift_up(self, index):

		while index != 0 and self._heap[self.parent(index)] < self._heap[index]:
			self._heap[self.parent(index)], self._heap[index] = self._heap[index], self._heap[self.parent(index)]
			index = self.parent(index)

	def size(self):
		return len(self._heap)

	def _sift_down(self, index):
		swap_index = index
		
		left = self.left_child(index)
		if self.size() > left and self._heap[swap_index] < self._heap[left]:	
			swap_index = left

		right = self.right_child(index)
		if self.size() > right and self._heap[swap_index] < self._heap[right]:
			swap_index = right

		if swap_index != index:
			self._heap[swap_index], self._heap[index] = self._heap[index], self._heap[swap_index]
			self._sift_down(swap_index)

	def insert(self, element):
		self._heap.append(element)
		self._sift_up(self.size() - 1)

	def extract_max(self):

		if self.size() == 1:
			return self._heap.pop()

		if self.size() != 0:
			result = self._heap[0]
			self._heap[0], self._heap[self.size() - 1] = self._heap[self.size() - 1], self._heap[0]
			self._heap.pop()
			self._sift_down(0)	
			return result

	def remove_index(self, index):
		if index == self.size() - 1:
			return self._heap.pop()

		res = self._heap[index]
		self._heap[index], self._heap[self.size() - 1] = self._heap[self.size() - 1], self._heap[index]
		self._heap.pop()
		self._sift_down(index)
		return result

	def get_max(self):
		if self.size():
			return self._heap[0]

	def is_empty(self):
		return self.size() == 0

	def change_priority(self, index, new_prio):
		old_prio = self._heap[index]
		self._heap[index] = new_prio

		if old_prio > new_prio:
			self._heap._sift_down(index)
		else:
			self._heap._sift_up(index)
		
		return old_prio

	
def heapify(array):
	heap = heapq(array)
	for i in reversed(range(0, len(array) // 2)):		
		heap._sift_down(i)

	print(heap._heap)

def heap_sort(array):
	heap = heapq()
	for i in array:
		heap.insert(i)

	for i in reversed(range(0, len(array))):
		array[i] = heap.extract_max()
		
	return array
if __name__ == "__main__":
	import doctest
	import time
	start = time.time()
	print("Testing...")
	doctest.testmod()
	print("Tested status - 200 OK")
	print(f"Time to test: {round(time.time() - start, 10)} ms")
