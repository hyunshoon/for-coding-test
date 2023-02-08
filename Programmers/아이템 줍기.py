'''
Point
- 외곽선을 긋는 경우  vs  (x,y)에서 시작하여 갈림길을 잘 판별하여 가는경우 vs (x,y)에서 시작하여 모든 갈림길을 BFS 하는 경우
- 마지막 경우로 구현 가능(외곽선). BFS로 풀어야 함.

Sol)
1. 사각형의 모든 점을 찍어야 한다
2. BFS로 상하좌우 탐색

Caution)
A. 사각형이 겹쳐서 가려지는 점을 제거해야한다(제거 안하면 지름길이 생김) && 만나는 점은 제거하면 안된다
A.a rectangle 배열을 기준으로 특정 점 (a,b)가 사각형 내부(경계 x)에 있는 경우 제거

Problem)
1.A.a 로 제거 못하는 내부 점이 있다. 예제1번의 (6,6), (6,4) 같은 경우 제거하지 못하고 외곽선에 포함되게 된다. -> 하지만 최단경로가 아니므로 무시해도 된다.
2. 연결되있지 않지만 인접해 있는 곳으로 바로가는 문제가 생긴다. 
2.1 이를 해결하기 위해 좌표를 모두 2배 늘린다.
'''
from collections import deque

def BFS(dots, x,y, item_x, item_y):
    #상하좌우
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    dots = set(dots)
    queue = deque()
    queue.append((x,y,0))
    
    visit = set()
    visit.add((x,y))
    
    while queue:
        x, y, cnt = queue.popleft()
        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y
            if cx < 0 or cy<0:continue # index_error
            if (cx,cy) == (item_x, item_y):
                return (cnt+1)//2 # 좌표를 2배 해줬으므로
            if (cx,cy) in visit:continue
            if (cx,cy) in dots:
                visit.add((cx,cy))
                queue.append((cx,cy,cnt+1))
            
def solution(rectangle, characterX, characterY, itemX, itemY):
    characterX *=2
    characterY *=2
    itemX *=2
    itemY *=2
    
    dots = []
    for rec in rectangle:
        x1 = rec[0] *2
        y1 = rec[1] *2
        x2 = rec[2] *2
        y2 = rec[3] *2
        #점을 찍는 과정 사각형은 네 변으로 이루어지기 때문에 4개
        temp1 = [(cur_x,y1) for cur_x in range(x1,x2+1)]
        temp2 = [(cur_x,y2) for cur_x in range(x1,x2+1)]
        temp3 = [(x1,cur_y) for cur_y in range(y1+1,y2)]
        temp4 = [(x2,cur_y) for cur_y in range(y1+1,y2)]
        
        dots.extend(temp1)
        dots.extend(temp2)
        dots.extend(temp3)
        dots.extend(temp4)
    final_dots = []
    for dot in dots:
        x = dot[0]
        y = dot[1]
        cnt = 0
        #임의의 점이 어떤 사각형의 내부에도 포함되면 안된다.
        for rec in rectangle:
            min_x = rec[0] *2
            min_y = rec[1] *2
            max_x = rec[2] *2
            max_y = rec[3] *2
            if min_x< x < max_x and min_y< y < max_y:
                cnt+=1
                break
        if cnt ==0:
            final_dots.append(dot)
                
    answer = BFS(final_dots, characterX, characterY, itemX, itemY)
    return answer
