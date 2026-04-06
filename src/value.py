# This handles dynamic programming to figure out the value
def value(char_vals, str_a, str_b):
    # char_vals is a dictionary
    # strings a and b
    
    # Citation: https://www.geeksforgeeks.org/python/python-using-2d-arrays-lists-the-right-way/
    rows, cols = len(str_a), len(str_b)
    # use +1 to avoid dp recursion out of bounds
    dp = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
    maxValue = 0

    # Bottom Up
    for i in range(1,rows+1):
        for j in range(1,cols+1):
            # (Base) Case 1: Do not match
            if str_a[i-1] != str_b[j-1]:
                dp[i][j] = 0

            # Case 2: Characters match
            else:
                # OPT(i,j) = charValue + OPT(i-1, j-1)

                charValue = char_vals[str_a[i-1]]
                dp[i][j] = charValue + dp[i-1][j-1]
                maxValue = max(maxValue, dp[i][j])

    return dp, maxValue #dp array is for backtracking