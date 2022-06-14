
### 간선이 없는 점을 고려해야한다. <- 이것 때문에 시간 많이 감
from collections import deque
N, M = map(int, input().split())
visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]

def bfs(x):
    queue = deque([x])
    visited[x] = True
    while queue:
        node = queue.popleft()
        for v in graph[node]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)


for _ in range(M):#그래프 초기화
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
count = 0
for i in range(1, N+1):
    if not visited[i]:
        if not graph[i]:
            visited[i] = True
            count += 1
        else:
            bfs(i)
            count +=1
print(count)