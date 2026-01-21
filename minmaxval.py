list=[10,20,3,30,40,200,50]
max=list[0]
min=list[0]
for x in list:
    if x>max:
        max=x
    if x<min:
        min=x
    
print(min)
print(max)