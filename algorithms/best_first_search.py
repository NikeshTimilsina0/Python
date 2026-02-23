import heapq

def best_first_search(graph, start, goal, heuristics):
    priority_queue = [(heuristics[start], start)]
    visited = set()
    path = []

    while priority_queue:
        h_val, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue
            
        visited.add(current_node)
        path.append(current_node)

        if current_node == goal:
            return path

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristics[neighbor], neighbor))

    return "Path not found"

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': ['G'],
    'G': []
}


heuristics = {
    'A': 6, 'B': 4, 'C': 4, 'D': 5, 'E': 2, 'F': 1, 'G': 0
}

result = best_first_search(graph, 'A', 'G', heuristics)
print(f"Best-First Search path to goal: {result}")