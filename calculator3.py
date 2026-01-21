def add(a,b):
    return a+b 
def sub(a,b):
    return a-b 
def mult(a,b):
    return a*b 
def div(a,b):
    return a/b 

operators={
    "+":add,
    "-":sub,
    "*":mult,
    "/":div
}

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
op=input("Enter the operator to use (+,-,*,/): ")

if op in operators:
    result=operators[op](num1,num2)
    print(result)
else:
    print("Invalid operator! Enter a valid one.")