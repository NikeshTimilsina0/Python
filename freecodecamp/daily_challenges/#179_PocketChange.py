"""Pocket Change
Given an array of integers representing the coins in your pocket, with each integer being the value of a coin in cents, return the total amount in the format "$D.CC".

100 cents equals 1 dollar.
In the return value, include a leading zero for amounts less than one dollar and always exactly two digits for the cents."""
def count_change(change):
    total=0
    for i in change:
        total+=i
    print(f'${total/100}')
    return f'${total/100:.2f}'
count_change([10, 5, 1, 10, 1, 25, 1, 1, 5, 1, 10])