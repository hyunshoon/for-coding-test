'''
N <= 10 이므로 시간복잡도 O(N^3) 가능
Goal: 순회할 때 드는 가장 적은 비용 찾기

제한 조건
- 재방문 불가. 마지막에 시작점으로 돌아오는 것은 가능.
- 시작 도시 정해져있지 않음.

Process)
1. N개의 출발점 모두 고려
2. 출발점에서 방문 가능한 도시 모두 방문
3. 방문했던 곳 제외하고 나머지 도시 모두 방문
4. 3번 완료 했다면 출발점으로 방문. 출발점으로 방문 성공시 카운트
'''
from collections import deque

N = int(input())
W = [list(map(int, input().split(' '))) for _ in range(N)]

answer = 1000000*20

def travel(cur_site, cnt, start_point, price):
    global answer
    visited = [False] * N
    queue = deque()
    queue.append((cur_site, cnt, visited, price))

    while queue:
        # print(len(queue))
        cur_site, cnt, visited, price = queue.popleft()
        if cnt > N-1:
            break
        for next_site in range(N):
            if visited[next_site] == True: continue
            if W[cur_site][next_site] == 0: continue
            if next_site == start_point and cnt == N-1: # 다음 방문이 마지막 방문이고 첫 지점이라면 순회 완료 된 것
                # print(cur_site, cnt, visited, price)
                answer = min(answer, price + W[cur_site][next_site])
            else:
                temp_visited = visited.copy()
                temp_visited[next_site] = True
                # print(id(temp_visited), id(visited))
                queue.append((next_site, cnt+1, temp_visited, price + W[cur_site][next_site]))
                del temp_visited

for i in range(N):
    travel(i, 0, i, 0)
print(answer)
