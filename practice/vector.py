class Vector:
	
	def __init__(self, size = 16):
		self._vector = [0 for i in range(size)]
		self._capacity = size
		self._size = 0

	def _resize(self, capacity):
		new_vec = [0 for i in range(capacity)]
		self._capacity = capacity
		for i in range(self._size):
			new_vec[i] = self._vector[i]
		self._vector = new_vec

	def size(self):
		return self._size

	def capacity(self):
		return self._capacity

	def is_empty(self):
		return self._size == 0

	def at_index(self, index):
		if index >= self._size:
			return "Index range out of bounds"

		return self._vector[index]

	def push(self, item):
		if (self._size == self._capacity):
			self._resize(self._size * 2)

		self._vector[self._size] = item
		self._size += 1
	
	def insert(self, index, item):
		if (self._size == self._capacity):
			self._resize(self._capacity * 2)
		
		prev = item
		for i in range(index, self._size+1):
			temp = self._vector[i]
			self._vector[i] = prev
			prev = temp
		self._size += 1

	def pop(self):
		if (self._size == 0):
			return "No elements present"
		self._vector[self._size - 1] = 0
		self._size -= 1

		if self._size / self._capacity <= 1/4:
			self._resize(int(self._capacity/4))

	def delete(self, index):
		if index >= self._size:
			return "Index out of bounds"

		for i in range(index, self._size-1):
			self._vector[i], self._vector[i+1] = self._vector[i+1], self._vector[i]
		self.pop()
		if self._size / self._capacity <= 1 / 4:
			self._resize(int(self._capacity/4))

	def find(self, item):
		if self._size == 0:
			return 0

		for i in range(self._size):
			if self._vector[i] == item:
				return i
		return 0

	def remove(self, item):
		res = self.find(item)
		if res:
			self.delete(res)

		if self._size / self._capacity <= 1 / 4:
			self._resize(int(self._capacity/4))
		return res

	def __repr__(self):
		return f"Vector <{self._vector}>"

if __name__ == "__main__":
	import doctest
	print("Testing the module....")
	doctest.testmod()
	print("Tested the module")
	v = Vector()
	for i in range(30):
		v.push(i+1)
		print(v.capacity())
		print(v)

	for j in range(20):
		v.pop()
		print(v.capacity())
		print(v)

