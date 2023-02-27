"""
Point)
- 방문할 수 있는 정점이 여러개인 경우 "번호가 작은 것 먼저" 방문
- 3번을 보면 그래프에 모든 정점이 표현되어있는 것이 아니다.
"""
import sys
from collections import defaultdict, deque
input = sys.stdin.readline
N, M, V = list(map(int, input().split()))

graph = defaultdict(list)
all_vertex = set()
for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    all_vertex.add(v1)
    all_vertex.add(v2)

def BFS(point):
    queue = deque()
    queue.append(point)
    result = [point]
    visit = set()
    visit.add(point)
    while queue:
        point = queue.popleft()
        next_lists = sorted(graph[point])
        for next_point in next_lists:
            if next_point in visit:continue
            queue.append(next_point)
            result.append(next_point)
            visit.add(next_point)
    return result

def DFS(point, result, visit):
    if len(result) == len(all_vertex):
        return result
    next_lists = sorted(graph[point])#번호가 낮은 것 우선
    for next_point in next_lists:
        if next_point in visit:continue
        visit.add(next_point)
        temp_visit = result.copy()
        temp_visit.append(next_point)
        a = DFS(next_point, temp_visit, visit)
        if a:
            return a
    
print(" ".join(map(str, DFS(V, [V], set({V})))))
print(" ".join(map(str, BFS(V))))
