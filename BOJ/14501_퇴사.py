'''
1 <= N <= 15
Ti: 걸리는 시간
Pi: pay
'''
N = int(input())
schedule = [(0,0)]
for i in range(N):
    schedule.append(list(map(int, input().split(' '))))#schedule[i][0]: Ti, schedule[i][1]: Pi
dp = [0] * 17

for i in range(N, 0, -1):
    if schedule[i][0] + i > N + 1:# 현재 수업을 들으면 시간초과 될 때
        dp[i] = dp[i+1]
    else:
        # max(현재 수업을 듣지 않는 경우, 듣는 경우)
        dp[i] = max(dp[i+1], schedule[i][1] + dp[i + schedule[i][0]])
print(dp[1])
