def dfs_iterative(adj_list, vertex):
	stack = [vertex]
	discovered = {i: False for i in adj_list.keys()}

	while stack:
		node = stack.pop()
		if discovered[node] == False:
			yield node
			discovered[node] = True
			for vertex in adj_list[node]:
				stack.append(vertex)
	
print(list(dfs_iterative({
	"A": ["B", "C"],
	"B": ["A", "D"],
	"C": ["A", "D", "E"],
	"D": ["B", "C"],
	"E": ["C"],
	}, "A")))

def dfs_rec(adj_list, vertex, discovered):
	discovered[vertex] = True
	yield vertex
	for node in adj_list[vertex]:
		if discovered[node] == False:
			yield from dfs_rec(adj_list, node, discovered)


def dfs_recursive(adj_list, vertex):
	discovered = {i: False for i in adj_list.keys()}
	return list(dfs_rec(adj_list, vertex, discovered))

print(dfs_recursive(
	{"A": ["B", "C"],
	"B": ["A", "D"],
	"C": ["A", "D", "E"],
	"D": ["B", "C"],
	"E": ["C"],
	}, "A"
	))