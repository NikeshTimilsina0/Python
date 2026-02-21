def fibonacci(n):
    
    sequence=[0,1]
    if n<=0:
        return 0
    if n<=len(sequence):
        return 1
    print(sequence)
    for i in range(2,n+1):
        next=sequence[i-1]+sequence[i-2]
        print(sequence)
        sequence.append(next)
    print(sequence)
    return sequence[n]
print(fibonacci(5))