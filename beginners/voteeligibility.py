name=input("Enter your name: ")
try:
    age=int(input("Enter your age: "))
    if age>=18:
        print(f"{name}, you are eligible to vote.")
    else:
        print(f"{name}, you are not eligible to vote.")
except ValueError:
    print("Invalid input. Please enter a valid age.")