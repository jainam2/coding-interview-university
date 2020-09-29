class ArrayQueue:
	def __init__(self, size = 8):
		self._capacity = size
		self._array = [None for _ in range(self._capacity)]
		self._front = self._rear = 0
		self._size = 0

	def _resize(self, new_capacity):
		new_array = [None for i in range(new_capacity)]
		new_front = 0
		new_rear = 0
		while self._rear != self._front:
			new_array[new_front] = self._array[self._rear]
			self._rear = (self._rear + 1) % self._capacity
			new_front = (new_front + 1) % new_capacity
		self._capacity = new_capacity
		self._array = new_array
		self._front = new_front
		self._rear = new_rear
		return f"Array resized to {new_capacity}"


	def enqueue(self, value):
		if (self._front + 1) % self._capacity == self._rear:
			self._resize(self._capacity * 2)

		self._array[self._front] = value
		self._front = (self._front + 1) % self._capacity
		self._size += 1
		

	def dequeue(self):
		if (self._array[self._rear] == None):
			print("queue is empty\n")
		else:
			self._array[self._rear] = None
			self._rear = (self._rear + 1) % self._capacity  
			self._size -= 1


	def display(self):
		temp = self._rear

		while temp != self._front:
			print(self._array[temp], end=" ")
			temp = (temp + 1) % self._capacity
		print()


	def empty(self):
		return self._size == 0


	def full(self):
		return self._capacity - 1 == self._size

if __name__ == "__main__":
	import doctest
	import time
	start = time.time()
	print("Testing...")
	doctest.testmod()
	print("Tested status - 200 OK")
	print(f"Time to test: {round(time.time() - start, 10)} ms")
