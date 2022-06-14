#1. 1이 되어 있는 곳에서 상하좌우 모두 갔다면 방문 처리해서 다시 계산 하지 않도록
#2. 첫 번째 큐 초기화 할 때 1이 되어있는 곳 모두 동시에 넣기
from collections import deque

col, row = map(int, input().split(' '))
init = []# row, col, day
graph = []
#상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for r in range(row):
    line = list(map(int, input().split(' ')))
    graph.append(line)
    for c in range(len(line)):
        if line[c] == 1:
            init.append((r, c, 0))

queue = deque(init)
result = 0
while queue:
    r, c, day = queue.popleft()
    for i in range(4):
        cr = dy[i] + r
        cc = dx[i] + c
        if cr<0 or cc<0 or cr>row-1 or cc> col-1:continue
        if graph[cr][cc] == 0:
            graph[cr][cc] = 1
            queue.append((cr, cc, day+1))
    result = day +1

fail = 0
for r in range(len(graph)):
    for c in range(len(graph[0])):
        if graph[r][c] == 0:
            fail = 1
            break
    if fail ==1:
        break
if fail ==1:
    print(-1)
else: 
    print(result-1)

