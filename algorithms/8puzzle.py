import heapq

goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

def manhattan(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_x = (val-1)//3
                goal_y = (val-1)%3
                distance += abs(i-goal_x) + abs(j-goal_y)
    return distance

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i,j

def generate_moves(state):
    x,y = find_blank(state)
    moves = []
    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    for dx,dy in directions:
        nx,ny = x+dx , y+dy
        if 0<=nx<3 and 0<=ny<3:
            new_state = [row[:] for row in state]
            new_state[x][y],new_state[nx][ny] = new_state[nx][ny],new_state[x][y]
            moves.append(new_state)

    return moves

def a_star(start):
    pq = []
    heapq.heappush(pq,(manhattan(start),0,start,[]))
    visited = []

    while pq:
        f,g,state,path = heapq.heappop(pq)

        if state == goal:
            print("Solution Found!\n")
            for step in path + [state]:
                for row in step:
                    print(row)
                print()
            print("Total Moves:", g)
            return

        visited.append(state)

        for move in generate_moves(state):
            if move not in visited:
                heapq.heappush(pq,
                    (g+1+manhattan(move),
                     g+1,
                     move,
                     path+[state]))

start = [[1,2,3],
         [4,0,6],
         [7,5,8]]

a_star(start)