name=input("Enter a name: ")
age=int(input("Enter your age: "))
email=input("Enter your email: ")

diction={
    "name":name,
    "age":age,
    "email":email
}
#print(diction)
for key,value in diction.items():
    print(f"{key.capitalize()}:{value}")