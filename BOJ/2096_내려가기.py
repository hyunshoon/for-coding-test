'''
key point
- 현재 줄의 선택이 다음 줄의 선택에도 영향을 미친다.
- 

variables
- dp
- points
점화식: 
dp[i][0] = point[i][0] + max(dp[i-1][0], dp[i-1][1])
dp[i][1] = point[i][0]
dp[i][2] = 
'''

N = int(input())
points = []
dp = [0 for _ in range(3)] * N
for i in range(N):
    points.append(list(map(int, input().split(' '))))

print(dp)