#if you have a list of elements and you have to insert a 
list=[1,2,4,5,34,23,3425,96]
sorted_list=sorted(list)
print(list)
print(sorted_list)
try:
    number=int(input('Enter the number to insert into the list: '))
except TypeError:
    print('Please enter a number only')