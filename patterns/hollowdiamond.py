def print_row(i,rows,a,b):
    print(' ' * (rows - i - 1), end='')
    if i == 0:
        print(f'{a}')
    else:  # Middle rows
        print(f'{a}' + ' ' *(2*i-1)  + f'{b}')
rows = 7


for i in range(rows):
    print_row(i,rows,"1","9")
for j in range(rows-2,-1,-1):
    print_row(j,rows,"1","9")
    
    
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *