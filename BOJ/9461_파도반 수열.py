"""
나선에서 가장 긴 변의 길이를 추가하는 것이 파도반 수열

Point)
1, 1, 1, 2, 2/, 3, 4, 5, 7, 9,/ 12, 16, 21
1, 1, 1, 1+1, 1+1, 1+2, 1+3, 1+4, 2+5, 2+7, 3+9, 4+12, 5+16, 

arr[i] = arr[i-1] + arr[i-5] (i>5) 부터 만족
"""
T = int(input())
dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2

for i in range(6,101):
    dp[i] = dp[i-1] + dp[i-5]

for _ in range(T):
    N = int(input())
    print(dp[N])
