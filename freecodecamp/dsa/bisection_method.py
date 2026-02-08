def square_root_bisection(number,tolerance=1e-7,max_iteration=100):
    
    if number<0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    elif number == 0 or number == 1:
        print(f'The square root of {number} is {number}')
        return number
    else:
        low,high=0,max(1,number)
        iteration=0
        while (high-low)>tolerance:
            iteration+=1
            if iteration>=max_iteration:
                print(f'Failed to converge within {max_iteration} iterations')
                return
            mid=(low+high)/2
            if mid*mid<number:
                low=mid
            else:
                high=mid
        result=(high+low)/2
        
        print(f'The square root of {number} is approximately {result}')
        return result