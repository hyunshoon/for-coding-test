'''
프로세스:
dp[k] = 가치의 합이 k원이 될 수 있는 동전의 개수 최솟값
dp[k] = min(dp[k-coins[0]] + dp[k-coins[1]] + ... + dp[k-coins[n]])

제한사항:
dp[k-coins[i]] == 0 이라면 해당 값은 포함하지 않는다. 
모든 dp[k-coins[i]]값이 0이라면 해당 dp[k]는 0 이 된다.

시간복잡도: O(n*k) n<=100, k<=10000

런타임에러 주의사항: k값을 고려하여 dp[0] * 10001로 초기화 했었는데 n의 최대 값 만큼 초기화 해야한다.
'''
n, k = map(int, input().split())
dp = [0] * 10003
coins = []
for i in range(n):
    coins.append(int(input()))
coins.sort()

for coin in coins:  # n원짜리 동전이 있다면 dp[n]=1
    dp[coin] = 1

for i in range(1, k + 1):
    temp_min = 1000000000
    is_valid = False #dp[i] 를 dp[i-coins[c]]로 초기화 하는지 체크
    if i in coins:continue # line 21 에서 정의.
    for c in range(n):
        if i - coins[c] < 1: continue
        if dp[i - coins[c]] != 0:
            temp_min = min(temp_min, dp[i - coins[c]] + 1)
            is_valid = True
    if is_valid:
        dp[i] = temp_min
    else:
        dp[i] = 0

if dp[k] == 0:
    print(-1)
else:
    print(dp[k])