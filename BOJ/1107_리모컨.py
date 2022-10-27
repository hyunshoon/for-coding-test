'''
1. 98 ~ 102는 +, - 가 가장 빠르다
cf) 1 같은 경우는 2.1번 방법이 가장 빠름
2.1 목적지로의 버튼이 고장난 것이 없을 때: 해당하는 버튼을 누르는게 최솟값
cf) 101 같은 경우는 1번 방법이 가장 빠름
2.2 목적지로의 버튼이 고장난 것이 있을 때:
목적지 N일 때 N-i, N+i 순으로 temp1, temp2 생성. 
2.2.1 temp1 or temp2 == N 이면 종료. answer = min(i + len(temp1), abs(N-100))
2.2.2 temp1 or temp2 != N 일 때, abs(N-100) == i 이면 answer = i

key point: 예외 처리 해줘야할 부분이 많다. 빼먹지 않고 예외처리 하는 방법은 케이스별로 반례를 적고, 예외에 가까운 수 들을 체크하는 방법 밖에는..?

시간복잡도: 
'''
def including_broken(N):
    if N <0:#temp1이 0보다 작아질 때 예외 처리
        return True
    broken_in_N = False
    for n in str(N):
        if int(n) in broken:
            broken_in_N = True
            break
    return broken_in_N

N = int(input())
M = int(input())

if M<1:
    answer = len(str(N))
    if 98 <= N <= 102:
        answer = min(abs(N-100), answer)
    print(answer)
else:
    broken = list(map(int, input().split(' ')))
    answer = 5000000
    list_n = [int(s) for s in str(N)] #number to list
    broken_in_N = including_broken(N)
    if not broken_in_N: # 목적지 N을 구성하고 있는 버튼이 고장난 것이 없다면
        answer = min(len(str(N)), abs(N-100))
    else: # 목적지 N을 구성하고 있는 버튼이 고장난 것이 있을 때
        for i in range(max(N,101)):
            temp1 = N - i
            temp2 = N + i
            if not including_broken(temp1) :# 목적지 N에서 i 만큼 이동 후 버튼 눌러 완료
                answer = min(i+len(str(temp1)), abs(N-100))
                break
            elif not including_broken(temp2):
                answer = min(i+len(str(temp2)), abs(N-100))
                break
            elif abs(N-100) == i: # 출발지에서 목적지 N까지 방향키만으로 도달
                answer = i
                break
    print(answer)


'''
0
10
0 1 2 3 4 5 6 7 8 9

500000
2
3 4 5

500000
10
0 1 2 3 4 5 6 7 8 9

100
10
0 1 2 3 4 5 6 7 8 9

999
1
9  <- 결과가 5가 나와야하는데 4가 나옴.
'''