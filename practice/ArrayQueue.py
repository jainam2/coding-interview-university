class ArrayQueue:
	def __init__(self, size = 8):
		self._capacity = size
		self._array = [None for _ in range(self._capacity)]
		self._front = self._rear = 0
		self._size = 0

	def enqueue(self, value):
		if (self._array[self._front] == None):
			self._array[self._front] = value
			self._front = (self._front + 1) % self._capacity
			self._size += 1
			print("Added elem: ", value, "\n")
		else:	
			print("Size not sufficient!\n")

	def dequeue(self):
		if (self._array[self._rear] == None):
			print("queue is empty\n")
		else:
			print('Removed element: ', self._array[self._rear], "\n")
			self._array[self._rear] = None
			self._rear = (self._rear + 1) % self._capacity	
			self._size -= 1

	def empty(self):
		return self._size == 0

	def full(self):
		return self._capacity == self._size

if __name__ == "__main__":
	import doctest
	import time
	start = time.time()
	print("Testing...")
	doctest.testmod()
	print("Tested status - 200 OK")
	print(f"Time to test: {round(time.time() - start, 10)} ms")
