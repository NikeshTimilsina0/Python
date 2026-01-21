num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
operator=input("Enter operator(+,-,*,/): ")
if operator=="+":
    num3=num1+num2
    print(num3)
elif operator=="-":
    num3=num1-num2
    print(num3)
elif operator=="*":
    num3=num1*num2
    print(num3)
elif operator=="/":
    num3=num1/num2
    print(num3)
else:
    print("Invalid operator!")