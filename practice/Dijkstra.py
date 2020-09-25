import heapq

# Dijkstra shortest path algorithm using priority queue.

def Dijkstra(Graph,  Source):
	dist = {Source: 0}
	prev = {}
	Q = []
	heapq.heapify(Q)

	for vertex in range(len(Graph)):
		if vertex != Source:
			dist[vertex] = float('inf')
		prev[vertex] = None
	heapq.heappush(Q, [dist[Source], Source])

	while Q:
		print(Q)
		u = heapq.heappop(Q)
		for vertex in range(len(Graph)):
			if Graph[u[1]][vertex] != 0: 
				alt = dist[u[1]] + Graph[u[1]][vertex]	
				if alt < dist[vertex]:
					dist[vertex] = alt
					prev[vertex] = u[1]
					heapq.heappush(Q, [alt, vertex])

	return dist, prev

def get_minimum_path(Graph, Source1, Source2):
	distance, path = Dijkstra(Graph, Source1)
	min_path = [Source2]
	try:
		while path[Source2] != Source1:
			Source2 = path[Source2]
			min_path.append(Source2)
		min_path.append(Source1)
		return min_path[::-1]
	except:
		return "Path does not exist!"

print(Dijkstra([[0, 6, 1, 0, 0, 0],
				[0, 0, 0, 5, 6, 3],
				[0, 3, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 2],
				[0, 0, 0, 1, 0, 0]], 0))

print(get_minimum_path([[0, 6, 1, 0, 0, 0],
				[0, 0, 0, 5, 6, 3],
				[0, 3, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 2],
				[0, 0, 0, 1, 0, 0]], 2, 3))
