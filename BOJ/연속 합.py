"""
Point)
- 음수가 주어진다고 연속 합을 멈추는게 아니다. EX) 10, -5, 20
- O(NlogN) or O(N)
- dp[i] = max(arr[i], arr[i] + dp[i-1])
"""
n = int(input())
num_list = list(map(int, input().split()))
dp = [0] * 100001
dp[0] = num_list[0]
result = dp[0]
for i in range(1,len(num_list)):
    dp[i] = max(num_list[i], num_list[i] + dp[i-1])
    result = max(result, dp[i])
print(result)
