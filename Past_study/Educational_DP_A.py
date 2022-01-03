N = int(input())
costs = list(map(int, input().split()))
dp = [0] * N 
for i in range(1, N, 1):
    if i - 2 < 0:
        dp[i] = dp[i-1] + abs(costs[i-1] - costs[i])
    elif i - 2 >= 0:
        dp[i] = min( (dp[i-1] + abs(costs[i-1] - costs[i])),\
                     (dp[i-2] + abs(costs[i-2] - costs[i])) ) 

print(dp[N-1]) 