'''
Info:5가지 도형. 회전, 대칭 고려했을 때 1+2+8*3 = 27개

구현 하는 방법
1. 27가지 case를 모두 따로 구현하는 방법. 가지수가 너무 많아서 pass
2. 핵심은 정사각형 '4개'를 이어붙인 것. 변끼리 연결되어있는 정사각형 4개를 이어붙인 도형은 27개다. 즉, 가능한 4개짜리 테트로미노는 27개이므로 테트로미노를 만드는 방법을 구현하면 된다.

테트로미노 구현 방법
(i,j)에서 가능한 테트로미노를 완전탐색으로 구현. (i,j)를 포함한 n가지의 서로다른 테트로미노를 상하좌우로 탐색

제한조건
1. 인덱스를 벗어났을 때 해당 길로 탐색 X
2. 정사각형 4개째에서 더이상 탐색 X
3. 이미 방문한 곳을 방문해도 되지만(블록철 모양을 만족하기 위해) 무한루프 돌지않게 제한 

시간복잡도 N=500 이므로
O(n^2)까지 만족
25000 * def(tetro)

Review
- 이런 탐색 문제는 디테일이 생명이다. 제한 조건들의 순서도 중요하게 고려. 
- listA = listB를 하면 call by value 가 아닌 call by reference 처럼 되므로 listA.append(1)을하면 listB에도 1이 추가 된다
- 블록철자 모양 때문에 반복 방문도 허락해야 한다. 주의 깊게 제시된 조건을 살피자. 중복 방문했을 때 추가는 하지 않지만 지나가게 해주는 코드 추가.

'''
N, M = map(int, input().split(' '))
maps = []

#상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]
answer = 0

def tetro(li, r, c, value):
    global answer
    for i in range(4): # 네 가지 경우의 수 중에 필터링 되는 것을 고르고 성공한 것은 가지치기를 잘 해야한다.
        cur_row = r + dr[i]
        cur_col = c + dc[i]
        if cur_row < 0 or cur_row > N-1 or cur_col < 0 or cur_col > M-1:# range 넘어 섰을 때 skip
            continue
        if (cur_row, cur_col) in li: # 이미 방문 했을 때 추가는 하지 않지만 지나가게 해줘야 한다.
            for j in range(4):
                skip_row = cur_row + dr[j]
                skip_col = cur_col + dc[j]
                
                if skip_row < 0 or skip_row > N-1 or skip_col < 0 or skip_col > M-1:continue
                if (skip_row, skip_col) in li:continue #무한루프 배제
                li.append((skip_row, skip_col))
    
                if len(li) == 4:
                    result = value + maps[skip_row][skip_col]
                    answer = max(answer, result)
                else: 
                    #테트로미노 완성체가 아니므로 한 번 더!
                    tetro(li, skip_row, skip_col, value + maps[skip_row][skip_col])
                li.pop()
        else:
            li.append((cur_row, cur_col))
    
            if len(li) == 4:
                result = value + maps[cur_row][cur_col]
                answer = max(answer, result)
            else: 
                #테트로미노 완성체가 아니므로 한 번 더!
                tetro(li, cur_row, cur_col, value + maps[cur_row][cur_col])
            li.pop()

for _ in range(N):
    row = list(map(int, input().split(' ')))
    maps.append(row)

for i in range(N):
    for j in range(M):
        tetro([(i, j)], i, j, maps[i][j])                
print(answer)
