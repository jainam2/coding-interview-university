class BinarySearchTree:

	class Node:
		def __init__(self, data):
			self.value = data
			self._parent = None
			self._left = None
			self._right = None

	def __init__(self):
		self._root = None
		self._size = 0

	def insert(self, data):
		new_node = self.Node(data)

		if (self._root == None):
			self._root = new_node

		else:
			curr_node = self._root
			
			while True:
				if new_node.value <= curr_node.value and curr_node._left !=None:
					curr_node = curr_node._left
					continue

				if new_node.value > curr_node.value and curr_node._right != None:
					curr_node = curr_node._right
					continue
					
				new_node._parent = curr_node
				if new_node.value <= curr_node.value:
					curr_node._left = new_node

				else:
					curr_node._right = new_node

				break
		self._size += 1

	def level_order_traversal(self):
		queue = [self._root]

		while queue:

			node = queue.pop(0)
			if node._left:
				queue.append(node._left)
			if node._right:
				queue.append(node._right)

			yield node.value

	def inorder_traversal(self):
		stack = []
		curr = self._root
		while stack or curr: 
			if curr:
				stack.append(curr)
				curr = curr._left
			elif stack:
				curr = stack.pop()
				yield curr.value
				curr = curr._right
			else:
				break

	def preorder_traversal(self):
		stack = [self._root]
		while stack:
			node = stack.pop()
			if node._right:
				stack.append(node._right)
			if node._left:
				stack.append(node._left)
			
			yield node.value

	def postorder_traversal(self):
		stack1 = [self._root]
		stack2 = []
		while stack1:
			node = stack1.pop()
			stack2.append(node)

			if node._left:
				stack1.append(node._left)
			if node._right:
				stack1.append(node._right)

		while stack2:
			yield stack2.pop().value

	def delete_tree(self):
		self._root = None

	def is_in_tree(self, value):
		curr = self._root
		while curr:
			if curr.value == value:
				return (True, curr)

			if curr.value > value:
				if curr._left:
					curr = curr._left
				else:
					return False
			else:
				if curr._right:
					curr = curr._right
				else:
					return False

	def get_height(self):
		queue = [self._root]
		height =0


		while queue:
			size = len(queue)

			while size > 0:
				node = queue.pop(0)
				if node._left:
					queue.append(node._left)
				if node._right:
					queue.append(node._right)
				size -= 1

			height += 1
		return height

	def get_min(self):
		curr = self._root
		while curr._left:
			curr = curr._left

		return curr.value

	def get_max(self):
		curr = self._root
		while curr._right:
			curr = curr._right

		return curr.value

	def is_bst(self):

		stack = [self._root]

		while stack:
			node = stack.pop()
			if node._left != None:
				if node.value >= node._left.value:
					stack.append(node._left)
				else:
					return False

			if node._right != None:
				if node._right != None:
					if node.value < node._right.value:
						stack.append(node._right)
					else:
						return False
				else:
					return False
		return True

	def get_successor(self, node):
		if node:
			node = node._right

			while node._left:
				node = node._left

			return node


	def delete_value(self, value):
		is_present = self.is_in_tree(value)
		if is_present:
			self.delete(is_present[1])


	def delete(self, node):

		parent_node = node._parent
		if node._left == None and node._right == None:
			
			if parent_node._left == node:
				parent_node._left = None
			else:
				parent_node._right = None


		elif node._left == None:
			if parent_node._right == node:
				parent_node._right = node._right
			elif parent_node._left == node:
				parent_node._left = node._right


		elif node._right == None:
			if parent_node._left == node:
				parent_node._left = node._left
			elif parent_node._right == node:
				parent_node._right = node._left

		else: 
			successor = self.get_successor(node)
			successor.value, node.value = node.value, successor.value
			self.delete(successor)


if __name__ == "__main__":
	import doctest
	import time
	start = time.time()
	print("Testing...")
	doctest.testmod()
	print("Tested status - 200 OK")
	print(f"Time to test: {round(time.time() - start, 10)} ms")