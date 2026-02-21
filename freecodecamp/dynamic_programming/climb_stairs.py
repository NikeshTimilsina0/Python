def climb_stairs_memo(n,memo={}):
    """Dynamic programming with memoization"""

    if n in memo:
        return memo[n]
    if n<=2:
        return n
    memo[n] = climb_stairs_memo(n-1, memo) + climb_stairs_memo(n-2, memo)
    print(memo)
    return memo[n]
print(climb_stairs_memo(5))