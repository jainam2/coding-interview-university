class LinkedList:

	class _Node:
		def __init__(self, element):
			self._value = element
			self._next = None

	def __init__(self):
		self._size = 0
		self._head = None

	def display(self):
		if self._head:
			curr = self._head
			while curr:
				print(curr._value, end=" -> ")
				curr = curr._next
			print(None)

	def size(self):
		return self._size

	def value_at(self, index):
		if self._size <= index:
			return None

		curr = self._head
		for i in range(0, index+1):
			curr = curr._next

		return curr._value

	def push_front(self, element):
		if not self._head:
			self._head = self._Node(element)

		else:
			new_node = self._Node(element)
			new_node._next = self._head
			self._head = new_node

		self._size += 1

	def pop_front(self):
		if self._head == None:
			return None
		else:
			temp = self._head
			self._head = self._head._next

		self._size -= 1
		return temp._value

	def push_back(self, element):
		if not self._head:
			self._head = self._Node(element)

		else:
			curr = self._head
			new_node = self._Node(element)
			while curr._next:
				curr = curr._next

			curr._next = new_node
		self._size += 1

	def pop_back(self):

		if self._head:
			curr = self._head
			prev = curr
			while curr._next:
				prev = curr
				curr = curr._next
			prev._next = None
			self._size -= 1
			return curr._value

		else:
			temp = self._head._value
			self._head = None
			self._size -= 1
			return temp

	def front(self):
		try:
			return self._head._value
		except:
			return None

	def back(self):
		if not self._head:
			return None

		curr = self._head
		while curr._next:
			curr = curr._next
		return curr._value

	def insert(self, index, element):
		if index > self._size:
			return False
		if  index == 0:
			self.push_front(element)
			self._size += 1
			return True

		new_node = self._Node(element)
		curr = self._head
		prev = curr
		while index:
			prev = curr
			curr = curr._next
			index -= 1

		new_node._next = prev._next
		prev._next = new_node
		self._size += 1

		return True

	def erase(self, index):
		if index > self._size:
			return None

		if index == 0:
			temp = self._head._value
			self._head = self._head._next
			self._size -= 1
			return temp

		curr = self._head
		prev = curr
		while index:
			prev = curr
			curr = curr._next
			index -= 1
		self._size -= 1
		prev._next = curr._next
		return curr._value

	def value_n_from_end(self, n):
		n = self._size - n
		if n<self._size:
			curr = self._head
			while n:
				curr = curr._next
				n -= 1
			return curr._value

	def find(self, element):
		if self._head == None:
			return False

		curr = self._head
		index = 0

		while curr._next and curr._value != element:
			curr = curr._next
			index += 1

		return (True, index) if curr._value == element else False

	def remove_value(self, element):
		sol = self.find(element)
		if sol:
			self.erase(sol[1])

	def reverse(self):
		prev = None
		curr = self._head
		while (curr):
			next = curr._next
			curr._next = prev
			prev = curr
			curr = next
		self._head = prev

if __name__ == "__main__":
	import doctest
	import time
	start = time.time()
	print("Testing...")
	doctest.testmod()
	print("Tested status - 200 OK")
	print(f"Time to test: {round(time.time() - start, 10)} ms")
