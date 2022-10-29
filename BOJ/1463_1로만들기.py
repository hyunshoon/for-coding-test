'''
Example)
1. 10 -> 9 -> 3 -> 1 : 최적 루트
2. 22 -> 11 -> 10 -> 9 -> 3 -> 1 # 여기서 10 -> 9 -> 3 -> 1 이 1번 예시이다. 즉 1번은 2번의 부분구조이다.
dp[n] = dp[n/3] + 1
dp[n] = dp[n/2] + 1
dp[n] = dp[n-1] + 1
N = 백만 이므로 시간복잡도는 O(n)까지 허용한다.
'''

N = int(input())

dp = [0] * 100000000
dp[1] = 0
for i in range(2, N+1):
    if i % 6 == 0:
        dp[i] = min(dp[i//3] +1, dp[i//2] + 1, dp[i-1] + 1)
    elif i % 3 ==0:
        dp[i] = min(dp[i//3] +1, dp[i-1] + 1)
    elif i % 2 ==0:
        dp[i] = min(dp[i//2] + 1, dp[i-1] + 1)
    else:
        dp[i] = dp[i-1] + 1
print(dp[N])
