from collections impot deque

def topolgical_sort(Graph):
	in_deg, Queue = {i: 0 for i in range(len(Graph))}, deque()
	for i in range(len(Graph)):
		for j in range(len(Graph)):
			if Graph[i][j] == 1:
				in_deg[j] += 1

	for k, v in in_deg.items():
		if v == 0:
			Queue.append(k)
	count = 0
	solution = []
	while Queue:
		vertex = Queue.popleft()
		count += 1
		solution.append(vertex)

		for node in range(len(Graph)):
			if Graph[vertex][node] == 1:
				in_deg[node] -= 1
				if in_deg[node] == 0:
					Queue.append(node)

	return solution if (count == len(Graph)) else "Solution not possible!"


print(topolgical_sort([
	[0, 1, 0, 0, 1], 
	[0, 0, 1, 1, 0], 
	[0, 0, 0, 0, 1], 
	[0, 0, 0, 0, 0], 
	[0, 0, 0, 1, 0]]))

