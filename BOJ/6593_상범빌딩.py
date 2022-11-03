'''
상범 빌딩은 3차원 배열로 이루어져 있다
L: 층
R: 행
C: 열
L, R, C <= 30
3차원 배열을 BFS로 탐색하며 S -> E 로 최종 도착

point
- 탐색하며 index 범위 초과한 곳은 탐색 x
- 방문한 곳은 다시 방문 x

problem
1. 입력 form을 열 간 공백이 있는줄 알았다.
2. minute(s)를 출력해야하는데 minutes(s)를 출력해서 뭐가 틀렸는지 계속 봄..
'''
from collections import deque
#동서남북상하
dl=[0,0,0,0,-1,1] # 하 이지만 l==0 이 꼭대기층 
dr=[0,0,1,-1,0,0]
dc=[1,-1,0,0,0,0]

def bfs(l, r, c, cnt):
    queue = deque()
    queue.append((l,r,c, cnt))

    while queue:
        l, r, c, cnt = queue.popleft()

        for i in range(6):
            cl = l + dl[i]
            cr = r + dr[i]
            cc = c + dc[i]
            
            if cl < 0 or cr < 0 or cc < 0 or cl > L-1 or cr > R-1 or cc > C-1:continue # 범위 초과
            if visited[cl][cr][cc] == True: continue # 방문한 곳
            
            if maps[cl][cr][cc] == '#':continue #벽
                
            elif maps[cl][cr][cc] == '.':
                visited[cl][cr][cc] = True # 방문처리
                queue.append((cl,cr,cc,cnt+1))

            if maps[cl][cr][cc] == 'E':#탈출
                print("Escaped in",cnt+1,"minute(s).")
                return 0

while True: 
    L, R, C = map(int, input().split(' '))
    if L ==0 and R== 0 and C==0: break # 종료 조건
    maps = []
    visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(L)] # 3차원 방문처리 배열 초기화

    for _ in range(L):
        floor = []
        for _ in range(R):
            string = input()
            floor.append(list(string.strip()))
        input()
        maps.append(floor)
    for z in range(L):
        for y in range(R):
            for x in range(C):
                if maps[z][y][x] == 'S': # S일 때 시작
                    result = bfs(z,y,x,0)
                    if result != 0: # 탈출 못하고 queue가 종료되면 trapped!
                        print('Trapped!')
    