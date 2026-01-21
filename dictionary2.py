users=[]
num=int(input("Enter the number of entries: "))
for i in range(1,num+1,1):
    print(f"Enter the {i}th set of entries: ")
    name=input("Enter name: ")
    age=int(input("Enter age: "))
    user={
        "name":name,
        "age":age
    }
    users.append(user)
    
print("\nThe available data: ")
for contents in users:
    print("\n")
    for key,value in contents.items():
        print(f"{key.capitalize()}:{value}")