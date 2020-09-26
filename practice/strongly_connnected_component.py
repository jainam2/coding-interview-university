class Kosaraju:

	def __init__(self, Graph):
		self.Graph = Graph
		self.stack = []
		self.seen = {i: False for i in range(len(Graph))}


	def dfs(self, vertex):
		if not self.seen[vertex]:
			self.seen[vertex] = True

			for node in range(len(self.Graph)):
				if Graph[vertex][node] == 1:
					self.dfs(node)
			self.stack.append(vertex)

	def strongly_connected_component(self):
		for vertex in range(len(self.Graph)):
			self.dfs(vertex)

		self.seen = {i: False for i in range(len(self.Graph))}

		for i in range(len(self.Graph)):
			for j in range(i+1, len(self.Graph)):
				self.Graph[i][j], self.Graph[j][i] = self.Graph[j][i], self.Graph[i][j]
		
		temp_stack = self.stack
		scc = 0

		while temp_stack:
			node = temp_stack.pop()
			if not self.seen[node]:
				scc += 1
				self.dfs(node)
		return scc

Graph = [[0, 1, 0, 0, 0],
		[0, 0, 1, 1, 0],
		[0, 0, 0, 0, 1],
		[1, 0, 0, 0, 0],
		[1, 0, 0, 0, 0]]

scc = Kosaraju(Graph)
print(scc.strongly_connected_component())
