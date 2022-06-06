from collections import deque

com_n = int(input())
network_n = int(input())

graph = [[] for _ in range(com_n+1)]
#graph 초기화
for n in range(network_n):
    x, y = list(map(int, input().split(' ')))
    graph[x].append(y)
    graph[y].append(x)
visited = [False] * (com_n+1)

queue = deque([1])
visited[1] = True
cnt = 0
while queue:
    v = queue.popleft()
    cnt+=1
    for i in graph[v]:
        if not visited[i]:
            queue.append(i)
            visited[i] = True
print(cnt-1)