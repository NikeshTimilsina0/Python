def bfs_graph_demo():
    # Representing the graph as an adjacency list
    graph = {
        1: [2, 3],
        2: [4, 5],
        3: [6],
        4: [],
        5: [],
        6: []
    }

    queue = [1]
    visited = {1}
    traversal_path = []
    print(graph)
    print("Starting BFS Traversal...")

    while queue:
        # Show the queue before we take the next element
        print(f"Current Queue: {queue}")
        
        # FIFO: Pop the first element added
        current = queue.pop(0)
        traversal_path.append(current)

        # Look at the "neighbors" of the current number
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return f"Final Path: {traversal_path}"

print(bfs_graph_demo())