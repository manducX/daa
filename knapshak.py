def knapsack(W, wt, val, n):
    # Initialize a 2D array K with dimensions (n+1) x (W+1)
    K = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for j in range(W+1):
            if i==0 or j==0:
                K[i][j] = 0
            elif wt[i-1] <= j:
                K[i][j] = max(val[i-1] + K[i-1][j-wt[i-1]], K[i-1][j])
            else:
                K[i][j] = K[i-1][j]
 
    return K[n][W]
W = int(input("Enter knapshak capacity:"))
wt = [10, 20, 30]
val = [60, 100, 120]
n = len(val)
print("Maximum value that can be obtained =", knapsack(W, wt, val, n))
