global visited

def dfs_rec(Graph, vertex, visited):
	visited[vertex] = True
	for node in range(len(Graph)):
		if Graph[vertex][node] == 1 and visited[node] == False:
			dfs_rec(Graph, node, visited)
	
def count_connected_component(Graph):
	connected_comp = 0
	visited = {i: False for i in range(len(Graph))}
	
	for vertex in range(len(Graph)):
		if visited[vertex] == False:
			dfs_rec(Graph, vertex, visited)
			connected_comp += 1
	return connected_comp

print(count_connected_component([
	[0, 0, 1, 1, 0],
	[0, 0, 0, 0, 0],
	[1, 0, 0, 1, 0],
	[1, 0, 1, 0, 0],
	[0, 0, 0, 0, 0]
]))
