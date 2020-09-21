from collections import deque

def breath_first_search(root, matrix):
    dist = {}
    for i in range(len(matrix)):
        dist[i] = float('inf')
    dist[root] = 0
    travsersal_order = []
    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()

        for i in range(len(matrix)):
            if matrix[node][i] == 1 and i != node and dist[i] == float('inf'):
                queue.append(i)
                dist[i] = dist[node] + 1
        travsersal_order.append(node)
    return dist, travsersal_order

print(breath_first_search(0,
[[1, 1, 1, 0, 0, 1],
 [1, 0, 1, 1, 1, 0],
 [1, 0, 1, 0, 0, 1],
 [0, 1, 0, 1, 0, 0],
 [0, 1, 0, 0, 1, 0],
 [1, 0, 1, 0, 0, 1]
]))
