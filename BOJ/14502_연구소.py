'''
0: 빈칸, 1: 벽, 2: 바이러스
3 <= N, M <= 8
바이러스 개수: 2~10
최대 8*8 인 map

Goal: 바이러스가 퍼지지않은 칸 개수의 최대 값

조건
1. 벽 3개를 필수적으로 세워야 한다.

point
- 어떤 빈칸에 벽을 세워야 바이러스를 최대한 안퍼지게 하는지 모른다. -> 임의의 칸을 고른다(빈칸 개수:a aC3)
- 골라진 임의의 칸을 모든 바이러스를 기준으로 bfs로 최대한 널리 퍼뜨린다.
'''
from itertools import combinations
from collections import deque
import copy 

N, M = map(int, input().split(' '))

# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

maps = []
blank_list = [] # 빈 칸 리스트가 있어야 임의의 벽 3개를 지을 곳을 조합으로 구할 수 있다.
virus_list = []

for i in range(N):
    row = list(map(int, input().split(' ')))
    for j in range(len(row)):
        if row[j] == 0:
            blank_list.append([i,j])
        elif row[j] == 2:
            virus_list.append([i,j])
    maps.append(row)

def bfs(new_walls):
    temp_maps = copy.deepcopy(maps)
    for wall in new_walls:
        temp_maps[wall[0]][wall[1]]  = 1
    visited = [[False] * M for _ in range(N)]
    queue = deque()
    for virus in virus_list:
        queue.append(virus)
        
    while queue:
        cr, cc = queue.popleft()
        for i in range(4):
            r = cr + dr[i]
            c = cc + dc[i]
            if r > N-1 or r < 0 or c > M-1 or c < 0: continue
            elif temp_maps[r][c] == 1 or temp_maps[r][c] == 2: continue
            elif visited[r][c] == True: continue
            else:
                temp_maps[r][c] = 2 # 빈 칸이 바이러스로 바뀜
                queue.append((r,c))
                visited[r][c] = True
    return temp_maps, visited

new_wall_li = list(combinations(blank_list, 3))
answer = 0
for wall in new_wall_li:
    completed_maps, temp_visited = bfs(wall)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if completed_maps[i][j] == 0:
                cnt += 1
    answer = max(answer, cnt)

print(answer)