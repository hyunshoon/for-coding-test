"""
지도가 주어질 때 이와 같이 제일 왼쪽 위 지점에서 출발하여 제일 오른쪽 아래 지점까지 항상 내리막길로만 이동하는 경로의 개수를 구하는 프로그램을 작성하시오.

첫째 줄에는 지도의 세로의 크기 M과 가로의 크기 N이 빈칸을 사이에 두고 주어진다. 이어 다음 M개 줄에 걸쳐 한 줄에 N개씩 위에서부터 차례로 각 지점의 높이가 빈 칸을 사이에 두고 주어진다. M과 N은 각각 500이하의 자연수이고, 각 지점의 높이는 10000이하의 자연수이다.

출력
첫째 줄에 이동 가능한 경로의 수 H를 출력한다. 모든 입력에 대하여 H는 10억 이하의 음이 아닌 정수이다.

Point)
- DFS로 탐색
- visit set을 파라미터에 포함
- M과 N은 각각 500이하의 자연수 <- DFS 로 풀면 시간초과. Memoization을 해야 된다.
"""
import sys
input = sys.stdin.readline
dc = [0,0,-1,1]
dr = [-1,1,0,0]
M, N = map(int, input().split())#세로 가로

maps = []

for _ in range(M):
    maps.append(list(map(int, input().split())))
answer = 0
def DFS(r,c,visit):
    global answer
    if (r,c) == (M-1,N-1):
        answer +=1        
    else:
        for i in range(4):
            cr = dr[i] + r
            cc = dc[i] + c
            if 0<=cr<M and 0<=cc<N:
                if (cr,cc) not in visit and maps[cr][cc] < maps[r][c]:
                    temp_visit = visit.copy()
                    temp_visit.add((r,c))
                    DFS(cr,cc,temp_visit)
            
DFS(0,0, set({(0,0)}))

print(answer)

################################### 여기까지 DFS 로만 푼 것. 시간초과 남
