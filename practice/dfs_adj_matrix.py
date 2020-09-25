def dfs_iterative(Graph, vertex):
	stack = [vertex]
	discovered = {i: False for i in range(len(Graph))}

	while stack:
		node = stack.pop()

		if discovered[node] == False:
			discovered[node] = True
			yield node

			for n in reversed(range(len(Graph))):
				if Graph[node][n] != 0:
					stack.append(n)

print(list(dfs_iterative(
		[[0, 1, 1, 1, 1],
		 [1, 0, 0, 0, 0],
		 [1, 0, 0, 0, 0],
		 [1, 0, 0, 0, 0],
		 [1, 0, 0, 0, 0]], 0)))


def dfs_rec(Graph, vertex, discovered):
	discovered[vertex] = True
	yield vertex
	for node in range(len(Graph)):
		if Graph[vertex][node] == 1 and discovered[node] == False:
			yield from dfs_rec(Graph, node, discovered)


def dfs_recursive(Graph, vertex):
	discovered = {i: False for i in range(len(Graph))}
	return list(dfs_rec(Graph, vertex, discovered))


print(dfs_recursive([[0, 1, 1, 1, 1],
		 [1, 0, 0, 0, 0],
		 [1, 0, 0, 0, 0],
		 [1, 0, 0, 0, 0],
		 [1, 0, 0, 0, 0]], 0))
