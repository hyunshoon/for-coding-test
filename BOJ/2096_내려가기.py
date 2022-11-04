'''
key point
- 현재 줄의 선택이 다음 줄의 선택에도 영향을 미친다.
- 메모리 관리

점화식: 
dp[i][0] = point[i][0] + max(dp[i-1][0], dp[i-1][1])
dp[i][1] = point[i][0] + max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
dp[i][2] = 마찬가지
min 값도 max값과 마찬가지로

시간복잡도: O(N)

Problem: 메모리초과. 
1. 직전 dp 값만 필요하지 모든 dp 값이 필요하지 않으므로 재사용하여 풀어본다.
2. dp를 직전 값만 사용하게 했지만 points 배열도 재사용하여 메모리 사용을 줄인다.
'''

N = int(input())
dp_min = [[0 for _ in range(3)] for _ in range(3)]
dp_max = [[0 for _ in range(3)] for _ in range(3)]

points = list(map(int, input().split(' ')))

dp_min[0][0] = points[0]
dp_min[0][1] = points[1]
dp_min[0][2] = points[2]

dp_max[0][0] = points[0]
dp_max[0][1] = points[1]
dp_max[0][2] = points[2]

for i in range(1, N):
    points = list(map(int, input().split(' ')))
    dp_max[1][0] = points[0] + max(dp_max[0][0], dp_max[0][1])
    dp_max[1][1] = points[1] + max(dp_max[0][0], dp_max[0][1], dp_max[0][2])
    dp_max[1][2] = points[2] + max(dp_max[0][1], dp_max[0][2])
    
    dp_max[0][0] = dp_max[1][0] # dp[0]  값을 현재 값으로 해주어야 다음 dp 값을 구할 수 있다.
    dp_max[0][1] = dp_max[1][1]
    dp_max[0][2] = dp_max[1][2]

    dp_min[1][0] = points[0] + min(dp_min[0][0], dp_min[0][1])
    dp_min[1][1] = points[1] + min(dp_min[0][0], dp_min[0][1], dp_min[0][2])
    dp_min[1][2] = points[2] + min(dp_min[0][1], dp_min[0][2])
    
    dp_min[0][0] = dp_min[1][0] # dp[0]  값을 현재 값으로 해주어야 다음 dp 값을 구할 수 있다.
    dp_min[0][1] = dp_min[1][1]
    dp_min[0][2] = dp_min[1][2]


max_value = max(dp_max[0][0],dp_max[0][1],dp_max[0][2])
min_value = min(dp_min[0][0],dp_min[0][1],dp_min[0][2])

print(max_value, min_value)