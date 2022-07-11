'''
점화식: Sn = max(An + An-1 + Sn-3, An + Sn-2, Sn-1)
'''
n = int(input())
glasses = [0]*10000
for i in range(n):
    glasses[i] = int(input())

dp = [0]*10000
dp[0] = glasses[0]
dp[1] = glasses[0] + glasses[1]
dp[2] = max(glasses[2]+dp[0], glasses[2] + glasses[1], dp[1])
for i in range(3, n):
    dp[i] = max(glasses[i] + glasses[i-1] + dp[i-3], glasses[i] + dp[i-2], dp[i-1])
print(dp[n-1])