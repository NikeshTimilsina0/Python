rows = 5

for i in range(rows):
    print(' ' * (rows - i - 1), end='')
    if i == rows - 1:  # First or last row
        print('*' * (2*rows-1))
    elif i == 0:
        print('*')
    else:  # Middle rows
        print('*' + ' ' *(2*i-1)  + '*')
  
#     *
#    * *
#   *   *
#  *     *
# *********