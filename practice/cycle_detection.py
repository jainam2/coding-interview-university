def dfs_rec(Graph, vertex, seen):
	if seen[vertex] == True:
		return True
	seen[vertex] = True
	for node in range(len(Graph)):
		if Graph[vertex][node] == 1:
			return dfs_rec(Graph, node, seen)

def cycle_detection(Graph, vertex):
	seen = {i: False for i in range(len(Graph))}
	return dfs_rec(Graph, vertex, seen)

if __name__ == "__main__":
	print(cycle_detection([
		[0, 1, 0, 0, 1], 
		[0, 0, 1, 1, 0], 
		[0, 0, 0, 0, 1], 
		[0, 1, 0, 0, 0], 
		[0, 0, 0, 1, 0]], 0))
