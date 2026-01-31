def findmax(numbers):
    max=numbers[0]
    for n in numbers:
        if n>max:
            max=n
    return max