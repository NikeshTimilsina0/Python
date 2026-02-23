def solve_queens(n):

    board=[[0]*n for _ in range(n)]

    def is_safe(r,c):
        for i in range(r):
            if board[i][c]: return 0
        i,j=r-1,c-1
        while i>=0 and j>=0:
            if board[i][j]: return 0
            i-=1; j-=1
        i,j=r-1,c+1
        while i>=0 and j<n:
            if board[i][j]: return 0
            i-=1; j+=1
        return 1

    def solve(r):
        if r==n:
            for i in board: print(i)
            return 1
        for c in range(n):
            if is_safe(r,c):
                board[r][c]=1
                if solve(r+1): return 1
                board[r][c]=0
        return 0

    solve(0)

solve_queens(5)