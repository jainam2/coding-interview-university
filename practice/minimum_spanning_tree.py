import heapq

def minimum_spanning_tree_adj_matrix(Graph, starting_vertex):  
	solution,heap, parent, discovered, dist = [], [], {}, {}, {}
	for i in range(len(Graph)):
		if i == starting_vertex:
			heap.append([0, starting_vertex])
			dist[i] = 0
		else:
			dist[i] = float('inf')
			parent[i] = None
		discovered[i] = False
		
	heapq.heapify(heap)	
	while heap:
		vertex = heapq.heappop(heap)

		if not discovered[vertex[1]]:
			solution.append(vertex[1])
			for node in range(len(Graph)):
				if Graph[vertex[1]][node] != 0 and not discovered[node]:
					if dist[node] > Graph[vertex[1]][node]:
						dist[node] = Graph[vertex[1]][node]
						parent[node] = vertex[1]
						heapq.heappush(heap, [dist[node], node])
			discovered[vertex[1]] = True
	print(solution)
	print(parent)
	print(dist)
	print(discovered)

	print()
	for k, v in parent.items():
		print(v, k, "->" ,Graph[k][v])

Graph = [[0, 2, 0, 6, 0],  
		[2, 0, 3, 8, 5], 
		[0, 3, 0, 0, 7],  
		[6, 8, 0, 0, 9], 
		[0, 5, 7, 9, 0]]

minimum_spanning_tree_adj_matrix(Graph, 0)



