from collections import deque
def bfs(x, y):
    graph[x][y] = 0
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y

            if cx<0 or cy<0 or cx>row-1 or cy> col-1:
                continue
            if graph[cx][cy] == 1:
                graph[cx][cy] = 0
                queue.append((cx, cy))
    return 1
#상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
T = int(input())

cnt_li = []
for _ in range(T):
    col, row, K = list(map(int, input().split(' ')))
    graph = [[0 for c in range(col)] for r in range(row)]
    for _ in range(K):#그래프 초기화
        x, y = list(map(int, input().split(' ')))
        graph[y][x] = 1
    cnt = 0
    for r in range(row):
        for c in range(col):
            if graph[r][c] == 1:
                cnt += bfs(r, c)
    cnt_li.append(cnt)
    
[print(c) for c in cnt_li]
