'''
N<=1000
i: 0 ~ N개
j: 0~9

점화식: dp[i][j] = dp[i-1][0] + ... + dp[i-1][j]

시간복잡도: O(n)
'''
N = int(input())

dp = [[0]*10 for _ in range(10000)]

for i in range(10):
    dp[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        for k in range(j+1):
            dp[i][j] += dp[i-1][k]

print(sum(dp[N])%10007)