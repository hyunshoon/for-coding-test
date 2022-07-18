'''
point: 어떻게 k값을 만들 것인가?
경우의 수 이므로 k-1원에서 k원으로 만드는 경우의수를 생각
'''
n, k = map(int, input().split())
values = []
dp = [0] * 10001
for _ in range(n):
    values.append(int(input()))
dp[0] = 1
for i in range(n):
    for j in range(k+1):
        if j-values[i]>=0:
            dp[j] += dp[j-values[i]]
print(dp[k])
    