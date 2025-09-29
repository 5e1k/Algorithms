from collections import deque

def bfs(graph, start, end):
    queue = deque([start])
    path = {start: 0}

    while queue:
        node = queue.popleft()

        if node == end:
            return path[node]
        
        for neigh in graph[node]:
            if neigh not in path:
                path[neigh] = path[node] + 1
                queue.append(neigh)
    
    return -1
