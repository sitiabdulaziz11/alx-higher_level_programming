def fibonacciVal(n):
    # Initialize the memo list with
    # appropriate size and base cases
    memo = [0] * (n + 1)
    memo[0] = 0
    memo[1] = 1
    
    # Fill the memo list with Fibonacci values
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    
    return memo[n]