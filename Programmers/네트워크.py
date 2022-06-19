#그래프 문제 고려요소
#1. 방문처리 어떻게 할 것인가
#2. 그래프 구조를 어떻게 짤 것인가
from collections import deque

def bfs(start, graph, visited):
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for g in graph[node]:
            if not visited[g]:#아직 방문하지 않았다면
                visited[g] = True #방문체크
                queue.append(g)

def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    for row in range(n):
        for col in range(n):
            if computers[row][col] == 1:
                graph[row].append(col)
                graph[col].append(row)
    visited = [False for _ in range(n)]
    
    for i, v in enumerate(visited):
        if not v:
            bfs(i, graph, visited)
            visited[i] = True
            answer += 1
        
    return answer