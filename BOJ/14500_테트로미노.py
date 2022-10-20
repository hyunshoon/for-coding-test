'''
Info:5가지 도형. 회전, 대칭 고려했을 때 1+2+8*3 = 27개

구현 하는 방법
1. 27가지 case를 모두 따로 구현하는 방법. 가지수가 너무 많아서 pass
2. 핵심은 정사각형 '4개'를 이어붙인 것. 변끼리 연결되어있는 정사각형 4개를 이어붙인 도형은 27개다. 즉, 가능한 4개짜리 테트로미노는 27개이므로 테트로미노를 만드는 방법을 구현하면 된다.

테트로미노 구현 방법

(i,j)에서 가능한 테트로미노를 완전탐색으로 구현. (i,j)를 포함한 n가지의 서로다른 테트로미노를 동서남북으로 탐색.
9C3


제한조건: 
1. 인덱스를 벗어났을 때 해당 길로 탐색 X
2. 정사각형 4개째에서 더이상 탐색 X
3. 1번을 만족해도 겹치는 테트로미노가 있다. 겹쳐도 딱히 문제 없다!
4. 

Review
- 이런 탐색 문제는 디테일이 생명이다. 제한 조건들의 순서도 언

재귀로 풀자

의사코드
def 테트로미노 구현
    for 

def 탐색 리스트
    for N행
        for M열
        테트로미노()
        
시간복잡도
O()
25000 * 


현재 트러블: 두번째 방문이 첫번째에서 위로가는걸로만 고정되어있다.
굳이 return을 시킬 필요 없다.

listA = listB를 하면 call by value 가 아닌 call by reference 처럼 되므로 listA.append(1)을하면 listB에도 1이 추가 된다.
블록철자 모양은 제한조건에 걸리게 된다.
중복 방문했을 때 추가는 하지 않지만 지나가게 해주는 코드 추가
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
            # print(li, (cur_row, cur_col), '범위 초과')
            continue
        if (cur_row, cur_col) in li: # 이미 방문 했을 때 추가는 하지 않지만 지나가게 해줘야 한다.
            #무한루프 돌지 않게 하려면
            
            
        else:
            li.append((cur_row, cur_col))
    
            if len(li) == 4:
                result = value + maps[cur_row][cur_col]
                answer = max(answer, result)
                print(answer, result, li)
                li.pop()
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






