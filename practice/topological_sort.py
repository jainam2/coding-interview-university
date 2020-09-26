import cycle_detection
from collections import deque

def topolgical_sort(Graph):
	for node in range(len(Graph)):
		if cycle_detection.cycle_detection(Graph, node):
			return "There is a cycle topolgical sort is not possible!"

	in_deg, Queue = {i: 0 for i in range(len(Graph))}, deque()
	for i in range(len(Graph)):
		for j in range(len(Graph)):
			if Graph[i][j] == 1:
				in_deg[j] += 1

	for k, v in in_deg.items():
		if v == 0:
			Queue.append(k)

	solution = []
	while Queue:
		vertex = Queue.popleft()
		solution.append(vertex)

		for node in range(len(Graph)):
			if Graph[vertex][node] == 1:
				in_deg[node] -= 1
				if in_deg[node] == 0:
					Queue.append(node)

	return solution

print(topolgical_sort([
	[0, 1, 0, 0, 1], 
	[0, 0, 1, 1, 0], 
	[0, 0, 0, 0, 1], 
	[0, 0, 0, 0, 0], 
	[0, 0, 0, 1, 0]]))
