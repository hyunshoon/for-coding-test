"""
Goal) 이분그래프 판별

Point)
- 그래프 구현
- 임의의 점을 시작으로 BFS든 DFS든 하면 될듯?
- set으로 두 집합 구현
    - 1번 집합에 연결되어있는 아직 집합에 포함되지 않은 점이 1번이라면 이분그래프 

Caution)
비연결 그래프 고려
"""
import sys
from collections import defaultdict, deque

def BFS(graph, A_set, B_set, point):
    def what_color(point):
        if point in A_set:
            return 'A'
        elif point in B_set:
            return 'B'
        else:#미정
            return 'N'
    
    queue = deque()
    queue.append((point, 'A'))
    A_set.add(point)
    while queue:
        point, color = queue.popleft()
        next_points = graph[point]
        for n_point in next_points:
            n_color = what_color(n_point)
            if n_color == color:#이분그래프 실패
                return 'NO'
            if n_color == 'N':#미정일 떄
                if color == 'A':
                    queue.append((n_point,'B'))
                    B_set.add(n_point)
                else:
                    queue.append((n_point, 'A'))
                    A_set.add(n_point)
input = sys.stdin.readline

K = int(input())

for _ in range(K):
    
    V, E = map(int, input().split())
    graph = defaultdict(list)
    
    for _ in range(E):#그래프 초기화
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    A_set = set()
    B_set = set()
    
    answer = "YES"
    for point in range(1,V+1):
        if point in A_set or point in B_set:
            pass
        else:
            temp = BFS(graph, A_set, B_set, point)
            if temp == 'NO':
                answer = "NO"
                break
    print(answer)
    
