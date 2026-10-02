def climbStairs(n: int) -> int:
    """
    main idea:

    at 'step n - 1',
        say you have 'x' unique ways to get there,
        then you MUST take 1 last step to get to 'n'.

        INTUITION:
        you have 'x' unique ways to get to get to 'n' from 'n - 1',
        because for any unique way to 'n - 1' (call it x_i; ex: 1 + 2 + 1 represented as steps taken),
        all you do is x_i + 1, and you're at 'n'
    
    at 'step n - 2',
        say you have 'y' ways to get there,
        then you take 2 steps to get to n.
        it's the same reasoning as 'step n - 1'.
        when you're on step n - 2, you take a fixed 2 steps to get to n
        NOTE: you could potentially take 1 step to get to 'step n - 1' BUT that unique path from 'step n - 2' to 'step n - 1' is already encapsulated in 'x'
    
    so therefore: the unique ways to get to 'step n' is ways(n - 1) + ways(n - 2)

    to solve this through DP memoization: 
        you keep a cache of {n: ways(n)}, and
        everytime you need climbStairs(n) you just ask,
        was it computed and saved to 'memo' as memo[n] before?
        if yes, then take that saved value and use it
        if no, then calculate it via 'ways(n - 2) + ways(n - 1)' AND THEN save it to 'memo' as memo[n]
    
        so when you do ways(6) = ways(5) + ways(4) -> ways(7) = ways(6) + ways(5)
        this 'chain' doesnt recalculate anything if implemented with DP
    """

    # solve through recursion + memoization
    """
    memo: dict[int, int] = {1: 1, 2: 2}

    def f(x):
        if x in memo:
            return memo[x]
        else:
            memo[x] = f(x - 1) + f(x - 2)
            return memo[x]

    return f(n)
    """

    # solve through tabulation + constant space
    first, second = 1, 1

    # given the ways(n) = ways(n - 1) + ways(n - 2) structure,
    #   we are taking a fibonacci approach to build the solution bottom up
    for i in range(n - 1):
        temp = first
        first += second
        second = temp

    return first
    

if __name__ == "__main__":
    output = climbStairs(3)
    print(output)