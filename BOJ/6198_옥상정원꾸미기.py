'''
조건
N <= 80000
관리인은 빌딩을 오른쪽 방향으로 본다. 자신이 위치한 빌딩 높이보다 높거나 같은 빌딩이 있으면 보지 못한다.

Sol)
1. i 번째에서 i + 1 ~ N 까지 탐색하여 값 비교 -> O(N^2)이므로 시간초과 가능성이 있다. 더 최적화 하는 법을 알아야 함.

point: 
다른 접근이 필요하다. 현재 들어오는 buliding에서 볼 수 있는 빌딩수를 구하는 것이 아니라, 이 빌딩을 볼 수 있는 빌딩수를 구하면 스택으로 풀 수 있다.

10 <- 첫 번째 인덱스므로 0
10 3 <- 3은 10에서 볼 수 있다. +1
10 7 <- 7은 3에서 볼 수 없지만 10에서 볼 수 있다. +1
10 7 4 <- 4는 7 과 10에서 볼 수 있다. +2
12 <- 12는 어디서도 볼 수 없다
12, 2 <- 2는 12에서 볼 수 있다. +1
'''

N = int(input())

buildings = []
stack = []
for _ in range(N):
    buildings.append(int(input()))

answer = 0
for building in buildings:
    while stack and stack[-1] <= building:
        stack.pop()
    answer += len(stack)
    stack.append(building)
print(answer)
    