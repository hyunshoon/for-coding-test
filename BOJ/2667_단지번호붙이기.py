#1의 값을 가진 포인트에서 시작해서 연결된곳을 전부 BFS로 순회
#한 섹터가 한가지 원소만 가질때 고려하지 못해서 자꾸 틀림.
from collections import deque

N = int(input())
graph = []
#상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for n in range(N):
    row = [int(r) for r in input()]
    graph.append(row)

def bfs(x, y):
    graph[x][y] = 0
    queue = deque()
    queue.append((x, y))
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y

            if cx<0 or cy<0 or cx>N-1 or cy> N-1:
                continue
            if graph[cx][cy] == 1:
                graph[cx][cy] = 0
                queue.append((cx, cy))
                cnt+=1
    return cnt

cnt_li = []
for row in range(N):
    for col in range(N):
        if graph[row][col] == 1:
            cnt_li.append(bfs(row, col))
cnt_li = sorted(cnt_li)
print(len(cnt_li))
[print(c) for c in cnt_li]

