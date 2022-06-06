from collections import deque

#상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = list(map(int, input().split(' ')))
graph = []

def bfs(x, y):
    queue = deque()    
    queue.append((x, y))
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #범위 벗어나면 취소
            if nx<0 or ny< 0 or nx > N-1 or ny> M-1:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[N-1][M-1]
for _ in range(N):
    row = [int(r) for r in input()]
    graph.append(row)

print(bfs(0, 0))

