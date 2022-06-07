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

            if cx<0 or cy<0 or cx>col-1 or cy> row-1:
                continue
            if graph[cx][cy] == 0:#아직 익지 않은 것
                graph[cx][cy] = graph[x][y] + 1
                queue.append((cx, cy))
                cnt+=1
    return cnt
#상, 하, 좌, 우

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

T = int(input())


for _ in range(T):
    col, row, K = list(map(int, input().split(' ')))
    col -= 1
    row -= 1
    graph = []
    for _ in range(K):#그래프 초기화
        x, y = list(map(int, input().split(' ')))
        graph[x][y] = 1
    
    for r in range(row):
        for c in range(col):
            if graph[row][col] == 1:
                bfs(row, col)
    
    


cnt_li = []

cnt_li = sorted(cnt_li)
print(len(cnt_li))
[print(c) for c in cnt_li]
