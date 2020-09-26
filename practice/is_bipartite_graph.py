from collections import deque

class Bipartite:
	def __init__(self ,Graph):
		self.graph = Graph
		self.colour = {i: 0 for i in range(len(Graph))}


	def is_bipartite(self):
		vertex = 0
		queue = deque()
		queue.append(vertex)
		self.colour[vertex] = "RED"

		while queue:
			node = queue.popleft()
			for neighbors in range(len(self.graph)):
				if self.graph[node][neighbors] == 1:
					if self.colour[neighbors] == 0:
						if self.colour[node] == "RED":
							self.colour[neighbors] = "BLUE"
						else:
							self.colour[neighbors] = "RED"

						queue.append(neighbors)
					
					elif self.colour[neighbors] == self.colour[node]:
						return False
		return True

bpt = Bipartite([[0,0,0,1,1],[0,0,0,1,1],[0,0,0,1,1],[1,1,1,0,0],[1,1,1,0,0]])
print(bpt.is_bipartite())
