rows = 5
cols = 5

for i in range(rows):
    if i == 0 or i == rows - 1:  # First or last row
        print('*' * cols)
    else:  # Middle rows
        print('*' + ' ' * (cols - 2) + '*',end='')
 