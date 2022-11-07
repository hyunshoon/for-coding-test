'''
Goal: 순회할 때 드는 가장 적은 비용 찾기

제한 조건
- 재방문 불가. 마지막에 시작점으로 돌아오는 것은 가능.
- 시작 도시 정해져있지 않음.

Process)
1. N개의 출발점 모두 고려
2. 출발점에서 방문 가능한 도시 모두 방문
3. 방문했던 곳 제외하고 나머지 도시 모두 방문
4. 3번 완료 했다면 출발점으로 방문. 출발점으로 방문 성공시 카운트

시간복잡도: O(N^3) N <= 10 이므로 시간복잡도 O(N^3) 가능
'''
N = int(input())
W = [list(map(int, input().split(' '))) for _ in range(N)]

answer = 1000000*20

def travel(cur_site, cnt, visited, start_point, price):
    global answer
    if cnt > N-1:
        return 0

    for next_site in range(N):
        if visited[next_site] == True: continue
        if W[cur_site][next_site] == 0: continue
        if next_site == start_point and cnt == N-1:
            answer = min(answer, price + W[cur_site][next_site])
        else:
            visited[next_site] = True
            travel(next_site, cnt+1, visited, start_point ,price + W[cur_site][next_site])
            visited[next_site] = False # 원래대로

for i in range(N):
    visited = [False] * N
    travel(i, 0, visited, i, 0)
print(answer)