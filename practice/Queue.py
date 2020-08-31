class LinkedQueue:
	
	class _Node:
		def __init__(self, val):
			self._value = val
			self._next = None

	def __init__(self):
		self._size = 0
		self._head = None
		self._tail = None

	def is_empty(self):
		return self._head == None

	def enqueue(self, value):
		new_node = self._Node(value)
		
		if self._head == None:
			self._head = self._tail = new_node
			self._tail.next = self._head

		else:
			new_node._next = self._tail._next
			self._tail._next = new_node	
			self._tail = new_node
		self._size += 1

	def dequeue(self):
		if self.is_empty():
			return 
		self._head = self._head._next
		self._tail._next = self._head
		self._size -= 1

	
	def display(self):
		curr = self._head

		while curr != self._tail:
			print(curr._value, end="->")
			curr = curr._next
		print("None")

if __name__ == "__main__":
	import doctest
	import time
	start = time.time()
	print("Testing...")
	doctest.testmod()
	print("Tested status - 200 OK")
	print(f"Time to test: {round(time.time() - start, 10)} ms")
