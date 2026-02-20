def climb_stairs_tabulation(n):
    """Dynamic programming with tabulation with O(n) time complexity"""
    if n<=2:
        return n
    dp=[0]*n
    print(dp)
    dp[0]=1
    dp[1]=2
    print(dp)

    for i in range(2,n):
        dp[i]=dp[i-1]+dp[i-2]
        print(dp)
    
    return dp[n-1]
print(climb_stairs_tabulation(10))