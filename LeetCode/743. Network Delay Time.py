'''
다익스트라 첫 문제. 이코테 코드.

다익스트라에서 그리디를 써야하는 걸 중점적으로 생각하자.
'''
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        for time in times:
            graph[time[0]].append([time[2], time[1]])#소요시간을 앞으로

        queue = []
        heapq.heappush(queue, (0,k))
        dist = defaultdict(int)
        
        while queue:
            time, node = heapq.heappop(queue)
            if node not in dist:
                dist[node] = time
                for new_time, new_node in graph[node]:
                    heapq.heappush(queue, (time+new_time, new_node))
        if len(dist) == n:
            return max(list(dist.values()))
        return -1
