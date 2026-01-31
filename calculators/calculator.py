num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
operator=input("Enter operator(+,-,*,/): ")
match operator:
    case "+":
        num3=num1+num2
        print(f"The sum of {num1} and {num2} is {num3}")
    case "-":
        num3=num1-num2
        print(f"The difference of {num1} and {num2} is {num3}")
    case "*":
        num3=num1*num2
        print(f"The multiplication of {num1} and {num2} is {num3}")
    case "/":
        num3=num1/num2
        print(f"The division of {num1} by {num2} is {num3}")
    