def dfs_n_queens(n):
    if n < 1:
        return []

    solutions = []
    stack = [[]]

    while stack:
        current_board = stack.pop()
        row = len(current_board)

        if row == n:
            solutions.append(current_board)
            visual_board = [['.' for _ in range(n)] for _ in range(n)]
            print(f"Solution {len(solutions)} Board:")
            for r, c in enumerate(current_board):
                visual_board[r][c] = 'Q'
                print(visual_board[r])
        
        for col in range(n - 1, -1, -1):
            
            is_safe = True
            for r, c in enumerate(current_board):
                if c == col or abs(r - row) == abs(c - col):
                    is_safe = False
                    break
            
            if is_safe:
                stack.append(current_board + [col])

    return sorted(solutions)

print("Final List of Solutions:",dfs_n_queens(4))