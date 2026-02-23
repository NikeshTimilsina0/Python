import heapq

graph = {
    'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'],
    'D': [], 'E': ['G'], 'F': ['G'], 'G': []
}

weights = {
    ('A', 'B'): 1, ('A', 'C'): 5,
    ('B', 'D'): 3, ('B', 'E'): 1,
    ('C', 'F'): 1, ('E', 'G'): 5,
    ('F', 'G'): 1
}

heuristics = {'A': 6, 'B': 4, 'C': 2, 'D': 5, 'E': 2, 'F': 1, 'G': 0}

def a_star_search(graph, start, goal, heuristics, edge_weights):

    priority_queue = [(heuristics[start], start)]
    
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    came_from = {}

    while priority_queue:
        current_f, current_node = heapq.heappop(priority_queue)

        if current_node == goal:
            return reconstruct_path(came_from, current_node)

        for neighbor in graph[current_node]:
            weight = edge_weights.get((current_node, neighbor), 1)
            tentative_g_score = g_score[current_node] + weight

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristics[neighbor]
                heapq.heappush(priority_queue, (f_score, neighbor))

    return None

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1] 


path = a_star_search(graph, 'A', 'G', heuristics, weights)
print(f"A* Path: {path}")