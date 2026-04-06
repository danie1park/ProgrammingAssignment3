# Citation: Logic is similar to the pseudocode of Sequence Alignment
def value(char_vals, str_a, str_b):
    # char_vals is a dictionary
    # strings a and b
    
    # Citation: https://www.geeksforgeeks.org/python/python-using-2d-arrays-lists-the-right-way/
    rows, cols = len(str_a), len(str_b)
    dp = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
    maxValue = 0

    # Bottom Up
    # start at 1 to avoid dp recursion out of bounds
    for i in range(1,rows+1):
        for j in range(1,cols+1):
            # Case 1: Move i (similar to gap)
            case1 = dp[i-1][j]

            # Case 2: Move j (similar to gap)
            case2 = dp[i][j-1]

            # Case 3: DP, consider value
            if str_a[i-1] == str_b[j-1]:
                charValue = char_vals[str_a[i-1]]
                case3 = charValue + dp[i-1][j-1]
            else:
                case3 = float('-inf') # dont consider

            dp[i][j] = max(case1, case2, case3)

    maxValue = dp[rows][cols]
    return dp, maxValue #dp array is for backtracking

def backtracking(dp, str_a, str_b):
    # find where maxValue was

    # walk backwards to recreate string

    return substring