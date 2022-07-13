'''
Goal: 에너지의 최솟값. 
점화식: An = min(An-1 + small, An-2 + big, An-3 + K)
point: K 사용여부를 같이 memo <- fail.
1. dp[i] = [min, false]
2. if dp[i][1] == false: 
point: K는 한 번 이므로 K를 고려하지 않고 dp를 만든 후에 어디서 K를 쓰면 가장 효율적인지 찾자
포기;
point: dp를 2차원배열로 만들고 dp[i][0]에는 큰 힘 쓰지않은 최소에너지 dp[i][1]에는 큰 힘 쓴 최소에너지 
'''
N = int(input())
energys = [[0,0] for _ in range(20)]
for i in range(N-1):
    small, big = map(int, input().split(' '))
    energys[i] = (small, big)
K = int(input())
dp = [[0, 0] for _ in range(21)]#에너지, 큰 힘 사용 여부
dp[1] = [0, 0]#1 번째 돌에 도달하기 위한 에너지
dp[2] = [energys[0][0], energys[0][0]]#2 번째 돌에 도달하기 위한 에너지
dp[3] = [min(dp[2][0] + energys[1][0], energys[0][1]),
        min(dp[2][0] + energys[1][0], energys[0][1])]

for i in range(4, N+1):
    #큰 힘 x -> 큰 힘 x or 큰 힘 O
    #큰 힘 O -> 큰 힘 O
    dp[i][0] = min(dp[i-1][0] + energys[i-2][0], dp[i-2][0] + energys[i-3][1])
    dp[i][1] = min(dp[i-3][0] + K, dp[i-1][1] + energys[i-2][0], dp[i-2][1] + energys[i-3][1])


print(min(dp[N][0], dp[N][1]))

'''
dp[1] = 0
dp[2] = energys[0][0]#2 번째 돌에 도달하기 위한 에너지
dp[3] = min(dp[2] + energys[1][0], energys[0][1])

for i in range(4, N+1):
    dp[i] = min(dp[i-1] + energys[i-2][0], dp[i-2] + energys[i-3][1])
max_diff = 0
for i in range(4, N+1):
    if dp[i] > dp[i-3] + K:#큰 힘을 사용했을 때 더 효과적.
        max_diff = max(dp[i] - (dp[i-3] + K), max_diff)
print(dp[N] - max_diff)
'''

'''
dp = [[0, False] for _ in range(N+1)]#에너지, 큰 힘 사용 여부
dp[1] = [0, False]#1 번째 돌에 도달하기 위한 에너지
dp[2] = [energys[0][0], False]#2 번째 돌에 도달하기 위한 에너지
dp[3] = [min(dp[2][0] + energys[1][0], energys[0][1]), False] 
for i in range(4, N+1):
    if dp[i-3][1] == True:# 큰 힘을 쓴 상태
        dp[i] = [min(dp[i-1][0] + energys[i-2][0], dp[i-2][0] + energys[i-3][1]), True]
    else:
        save_power = min(dp[i-1][0] + energys[i-2][0], dp[i-2][0] + energys[i-3][1])
        if save_power > dp[i-3][0] + K:
            dp[i] = [dp[i-3][0] + K, True]
print(dp[N][0])
'''