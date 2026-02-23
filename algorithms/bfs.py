from collections import deque

def bfs(graph, start_node):
    visited = {start_node}
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("Breadth-First Search starting from node 'A':")
bfs(graph, 'A')