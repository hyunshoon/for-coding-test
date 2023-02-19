'''
Point)
그래프는 어떻게 초기화 -> 딕셔너리
BFS로 완전 탐색하여 그래프의 거리 딕셔너리 생성 key(cnt):value(node 번호)
visit set으로 중복 방지 금지
answer_dict 로 그래프의 거리 딕셔너리 생성
'''
from collections import defaultdict, deque

def BFS(point, cnt, visit, graph):
    answer_dict = defaultdict(list)
    queue = deque()
    for g in graph[point]:
        queue.append((g, cnt))
        visit.add(g)
        answer_dict[cnt].append(g)
        
    while queue:
        new_point, cnt = queue.popleft()
        for new in graph[new_point]:
            if new in visit:continue
            queue.append((new, cnt+1))
            visit.add(new)
            answer_dict[cnt+1].append(new)
    return answer_dict
        
    
def solution(n, edge):
    visit = set([1])
    graph = defaultdict(list)
    for vertex in edge:
        graph[vertex[0]].append(vertex[1])
        graph[vertex[1]].append(vertex[0])
        
    answer_dict = BFS(1, 1, visit, graph)#point, cnt
    temp = list(answer_dict.keys())
    temp.sort(reverse=True)
    return len(answer_dict[temp[0]])
