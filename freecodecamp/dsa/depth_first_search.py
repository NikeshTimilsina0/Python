def dfs(adj_matrix,start_node):
    visited=[]
    stack=[start_node] 
    while stack:
        current=stack.pop()
        print('Current:',current)
        if current not in visited:
            visited.append(current)
            print(visited)
            for index,edge in enumerate(adj_matrix[current]):
                if edge==1 and index not in visited:
                    stack.append(index)
    return visited
print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1))
print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]], 3))
print(dfs([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], 0))