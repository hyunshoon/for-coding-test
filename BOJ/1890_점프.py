'''
목표: (0,0) 에서 시작해서 0 값을 가지는 (i,j)까지 가는 경우의 수

조건
1. 오른쪽이나 아래쪽으로만 점프
2. 점프할 때 방향을 바꾸면 안됌

(i,j) 값이 a라면 (i+a, i) =  

dp[i][j] = dp[i][j]로 올 수 있는 경우의 총 합
dp[0][0]부터 우측, 하단 방향으로 dp[a][b]값에 더해주면 된다.

dp[0][0] == value 라면
dp[value][0] += dp[0][0]
dp[0][value] += dp[0][0]
'''
N = int(input())
maps = []
for i in range(N):
    maps.append(list(map(int, input().split(' '))))

dp = [[0] * (N) for _ in range(N)]
dp[0][0] = 1

a, b = 0, 0
for i in range(N):
    for j in range(N):
        if maps[i][j] == 0: 
            a = i
            b = j
            break
        if dp[i][j] == 0: continue
        jump_range = maps[i][j]
        if i + jump_range < N:
            dp[i+jump_range][j] += dp[i][j]
        if j + jump_range < N:
            dp[i][j+jump_range] += dp[i][j]
        
print(dp[a][b])