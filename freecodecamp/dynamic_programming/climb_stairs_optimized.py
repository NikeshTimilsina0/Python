def climb_stairs_optimized(n):
    if n<=2:
        return n
    prev1,prev2=1,2
    for i in range(3,n+1):
        current=prev1+prev2
        prev1,prev2=prev2,current
    return prev2
        #[1,2,3,5,8,...]
print(climb_stairs_optimized(20))