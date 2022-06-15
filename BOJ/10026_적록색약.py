#색맹일때는 순회할 때 G -> R로 치환
from collections import deque

N = int(input())
#상하좌우
dx = [0,0,-1,1]
dy = [1,-1,0,0]

graph = []
for _ in range(N):#그래프 초기화
    row = input()
    temp = []
    for r in row:
        temp.append(r)
    graph.append(temp)

def bfs(r, c, is_blind, visited):
    queue = deque()
    queue.append((r,c))
    color = graph[r][c]
    if is_blind and color == 'G':
        color = 'R'
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            cr = dy[i] + r
            cc = dx[i] + c
            if cr <0 or cc < 0 or cr>N-1 or cc>N-1:continue
            if is_blind and graph[cr][cc] == 'G':
                graph[cr][cc] = 'R'
            if color != graph[cr][cc]:continue
            if visited[cr][cc] == False:
                visited[cr][cc] = True
                queue.append((cr, cc))
                
def cal_count(is_blind):
    visited = [[False for _ in range(N)] for _ in range(N)]
    cnt = 0
    for row in range(N):
        for col in range(N):
            if not visited[row][col]:#방문하지 않은 지점 방문 시작
                visited[row][col] = True
                bfs(row, col, is_blind, visited)
                cnt +=1
    return cnt

print(cal_count(False), cal_count(True))