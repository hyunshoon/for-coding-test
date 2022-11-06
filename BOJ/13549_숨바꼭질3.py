'''
Goal N -> K 로 가는 최단 시간
현재 지점에서 K 로의 최단 시간이 걸리는 경로를 알 수 없다! -> BFS로 해결
시간복잡도: O(N)
'''
from collections import deque
N, K = map(int, input().split())

visited = [False] * 200001
def searching(index):
    queue = deque()
    queue.append((index, 0))

    while queue:
        point, cnt = queue.popleft()

        if visited[point] == True: continue # 이미 방문한 곳이면 스킵
        if point < 0 or point > 100000: continue # 범위 초과
        if point == K:
            return cnt
        else:
            queue.append((point*2, cnt))
            queue.append((point-1, cnt+1))
            queue.append((point+1, cnt+1))
            visited[point] = True

print(searching(N))