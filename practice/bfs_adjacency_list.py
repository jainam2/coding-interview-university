from collections import deque

def breath_first_search(root, graph):
    dist = {}
    for node in graph.keys():
        dist[node] = float('inf')
    dist[root] = 0
    queue = deque()
    queue.append(root)
    travsersal_order = []
    while queue:
        node = queue.popleft()

        for child in graph[node]:
            if dist[child] == float('inf'):
                queue.append(child)
                dist[child] = dist[node] + 1
        travsersal_order.append(node)
    return dist, travsersal_order

print(breath_first_search(1, {
    1: [2, 3, 4, 11],
    2: [1, 6, 7],
    3: [1, 9],
    4: [11, 10, 1],
    5: [10],
    6: [2],
    7: [2],
    9: [3],
    10: [4, 5],
    11: [1, 4],
}))
