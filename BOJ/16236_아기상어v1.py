'''
v1.상좌우하로 BFS 했을 때 먹을 수 있는 물고기 바로 먹는 버전 
point: 물고기를 먹고나면 방문기록 초기화하고 graph와 상어 위치만 업데이트한다.
'''
from collections import deque
#상 좌 우 하
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]
N = int(input())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split(' '))))

def bfs(r, c, size, for_level_up, time):
    queue = deque()
    queue.append((r, c, 0))
    visit = [[False]*N for _ in range(N)]
    graph[r][c] = 0 #상어 초기 위치는 0으로 변경
    visit[r][c] = True #상어 초기 위치는 방문처리
    while queue:
        r, c, cur_time = queue.popleft()
        for i in range(4):
            cr = r + dr[i]
            cc = c + dc[i]
            if cr < 0 or cc < 0 or cr > N - 1 or cc > N - 1:
                continue
            if graph[cr][cc] < size and graph[cr][cc] > 0:  #자기보다 작으면 먹는다
                # for i in range(N):
                    # print("".join(list(map(str, graph[i]))))
                graph[cr][cc] = 0  #먹었으니까 0으로 처리
                time += (cur_time + 1)
                if for_level_up == size - 1:  #레벨업 할 때
                    size += 1
                    for_level_up = 0
                    # print('레벨업:', (cr, cc), '현재레벨:',size, '현재시간:',time)
                else:
                    for_level_up += 1  #못할 때 적립
                    # print('스택업:', (cr,cc), '현재레벨:',size, '현재시간:',time)
                return bfs(cr, cc, size, for_level_up, time)
            elif (graph[cr][cc] == 0 or graph[cr][cc] == size) and visit[cr][cc] == False:  #아무것도 없을 때
                visit[cr][cc] = True
                queue.append((cr, cc, cur_time + 1))
    return time

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            print(bfs(i, j, 2, 0, 0))
