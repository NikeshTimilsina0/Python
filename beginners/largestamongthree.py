num=[0,0,0]
largest=0
for i in range(0,3):
	num[i]=int(input(f"Enter number {i+1}"))
	if num[i] > largest:
		largest=num[i]
		
print(largest)