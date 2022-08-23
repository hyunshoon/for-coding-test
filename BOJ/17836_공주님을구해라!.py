#1. 그람을 쓰지 않을 때 
#2. 그람을 쓸 때 
#1, 2번 모두 try 하고 최솟값 return
# Error point: gram 을 가지지 않을 때 먼저 방문처리해서 gram을 가진 측이 방문 못하는 경우가 생긴다.
# sol) gram을 획득할 때 까지 방문했던곳을 획득 후에 다시 방문가능하게 해야 한다.

from collections import deque
#N:세로, M:가로, T: 제한시간
#공주위치:(N,M), 그람위치:2로 표시
N, M, T = map(int, input().split(' '))
graph = []
visit = [[False] * M for _ in range(N)]
visit_gram = [[False] * M for _ in range(N)]
for _ in range(N):
    row = list(map(int, input().split(' ')))
    graph.append(row)
#상하좌우
dr = [1,-1,0,0]
dc = [0,0,-1,1]

def bfs(T):
    queue = deque()
    if graph[0][0]==2:
        queue.append((0,0, True, 0))#위치, 그람 유무, 경과시간
    else:
        queue.append((0,0, False, 0))#위치, 그람 유무, 경과시간
        
    while queue:
        x, y, gram, time = queue.popleft()
        for i in range(4):
            x_cur = x + dc[i]
            y_cur = y + dr[i]
            if x_cur <0 or y_cur<0 or x_cur>M-1 or y_cur>N-1:
                continue
            if gram == True:
                if visit_gram[y_cur][x_cur] == False:
                    visit_gram[y_cur][x_cur] = True
                    queue.append((x_cur, y_cur, True, time+1))
            else:
                if graph[y_cur][x_cur] == 1 or visit[y_cur][x_cur] == True:
                    continue
                visit[y_cur][x_cur] = True
                if graph[y_cur][x_cur] == 2: # 그람 득템. 한 번만 실행. 이때, 기존 visit data를 visit_gram으로 copy하고 visit_gram은 별도로 방문 처리
                    queue.append((x_cur, y_cur, True, time+1))
                else: 
                    queue.append((x_cur, y_cur, False, time+1))
            if x_cur==M-1 and y_cur == N-1:
                return time +1 
            if time+1 > T:
                return "Fail" # 사간초과로 Fail
    return "Fail" # 순회 할 수 있는 곳 다해서 Fail
print(bfs(T))
                    
                
            