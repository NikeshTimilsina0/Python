from collections import deque

def waterjug(m, n, d):

    visited = set()
    parent = {}

    q = deque()
    q.append((0,0))
    visited.add((0,0))

    while q:
        x, y = q.popleft()

        if x == d or y == d:
            print("Solution Path:")
            path = []
            while (x,y) in parent:
                path.append((x,y))
                x,y = parent[(x,y)]
            path.append((0,0))
            path.reverse()
            for state in path:
                print(state)
            return

        next_states = [

            (m, y),
            (x, n),
            (0, y),
            (x, 0),

            (x - min(x, n-y), y + min(x, n-y)),
            (x + min(y, m-x), y - min(y, m-x))
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                parent[state] = (x,y)
                q.append(state)

    print("No Solution Possible")


m = 4
n = 3
d = 2

waterjug(m, n, d)