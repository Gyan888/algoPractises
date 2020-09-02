val = [60, 100,  120]
w = [10, 20, 30]
W = 50

### knapsack problem recursive approachs

def knapsack(W, n):
  if n == 0:
    return 0
  elif w[n-1] > W:
    return knapsack(W, n-1)
  else:
    return  max(val[n-1] + knapsack(W-w[n-1], n-1), knapsack(W, n-1))


print(knapsack(W, len(val)))