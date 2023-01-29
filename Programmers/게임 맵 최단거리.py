from collections import deque

#상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(maps):
    queue = deque()
    queue.append((0,0,1))
    
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    while queue:
        r, c, cnt = queue.popleft()
        
        for i in range(4):
            cr = r + dr[i]
            cc = c + dc[i]
            
            if cr <0 or cc <0 or cr > n-1 or cc > m-1:continue#범위 초과
            if maps[cr][cc] == 0 or visited[cr][cc] == True: continue #벽, 이미 들린 곳
            if cr == n-1 and cc == m-1:
                return cnt+1
            
            queue.append((cr,cc,cnt+1))
            visited[cr][cc] = True
            
    return -1

def solution(maps):
    answer = bfs(maps)
    return answer
