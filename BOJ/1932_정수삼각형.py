'''
dp[i][j]: (i,j)까지 도달하는 가장 큰 값
dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + scores[i][j]
point: 첫 번째 열과 마지막 열은 한 가지 경우의 수, 나머지는 두 가지 경우의 수
'''
N = int(input())
scores = [[-1]*N for _ in range(N)]
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        scores[i][j] = row[j]
dp = [[-1]*N for _ in range(N)]

dp[0][0] = scores[0][0]
dp[1][0] = dp[0][0] + scores[1][0]
dp[1][1] = dp[0][0] + scores[1][1]
for i in range(2, N):
    dp[i][0] = dp[i-1][0] + scores[i][0]
    dp[i][i] = dp[i-1][i-1] + scores[i][i]
    for j in range(1, i):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + scores[i][j]

print(max(dp[N-1]))