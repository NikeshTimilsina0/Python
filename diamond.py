for i in range(0, 5):
    for j in range(5 - i - 1):
        print('  ', end='')
    for k in range(2 * i + 1):
        print('* ', end='')
    print()
for l in range(4,0,-1):
    for m in range(l,5):
        print('  ',end='')
    for n in range(2*l-1):
        print('* ', end='')
    print()

#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *