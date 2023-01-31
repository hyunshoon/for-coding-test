'''
문제
세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.

말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다. 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.

입력
첫째 줄에 R과 C가 빈칸을 사이에 두고 주어진다. (1 ≤ R,C ≤ 20) 둘째 줄부터 R개의 줄에 걸쳐서 보드에 적혀 있는 C개의 대문자 알파벳들이 빈칸 없이 주어진다.

출력
첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.


시간초과 해결
알파벳의 방문처리를 효율적으로 하기위해 visited 를 list 자료형이 아닌 set 자료형으로 해결
'''

R, C = map(int, input().split())
maps = []
#상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]
answer = 0

def DFS(r, c, depth, visited):
    global answer
    for i in range(4):
        cr = dr[i] + r
        cc = dc[i] + c
        if 0<= cr < R and 0 <=cc < C and maps[cr][cc] not in visited:
            visited.add(maps[cr][cc])
            DFS(cr,cc,depth+1,visited)
            visited.remove(maps[cr][cc])
            answer = max(answer, depth+1)
    

for _ in range(R):
    row = [r for r in input()]
    maps.append(row)

DFS(0,0,1, set(maps[0][0]))
print(answer)
