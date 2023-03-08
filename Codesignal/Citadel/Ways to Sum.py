
# Python3 implementation to count
# ways to sum up to a given value N 

# Function to count the total  
# number of ways to sum up to 'N' 
def findSolution(n, m):
    numbersToAdd = []
    for x in range(m, n + 1):
        numbersToAdd.append(x)

    # init
    length = len(numbersToAdd)
    dp = [[0] * (length + 1) for x in range(n + 1)]
    dp[0] = [1] * (length + 1)

    for i in range(1, n + 1):
        for j in range(1, length + 1):
            if (i >= numbersToAdd[j - 1]):
                dp[i][j] = dp[i][j - 1] + dp[i - numbersToAdd[j - 1]][j]
            else:
                dp[i][j] = dp[i][j - 1]
    # import PrintMatrix as pm
    # pm.printMatrix(dp)
    return dp[n][length]

# Driver Code 
arr = [1, 2, 3]
m = len(arr)
N = 5
print(findSolution(N, m))
