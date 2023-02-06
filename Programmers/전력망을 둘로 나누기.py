'''
Point
모든 노드는 연결 돼 있다.
wires num = NC2 < 5000

Sol) 모든 wires를 끊는 방법이 가능한가? -> O(wires *N) 이므로 가능은하다.

1. 딕셔너리로 wires 그래프 생성
2. BFS로 visit 체크하며 탐색

Q)
visit 는 어떻게 구현? -> set으로 구현해서 빠르게 찾게함
'''
from collections import deque, defaultdict
def BFS(d_wires):
    visit = set()
    queue = deque()
    for k in d_wires.keys():
        if k:#빈 리스트가 아닌 임의의 키를 첫 출발지로 초기화
            queue.append(k)
            visit.add(k)
            break
    
    while queue:
        n1 = queue.popleft()
        for next_node in d_wires[n1]:
            if next_node in visit:
                continue
            else:
                visit.add(next_node)
                queue.append(next_node)

    return len(visit)
            
def solution(n, wires):
    answer = []
    d_wires = defaultdict(list)
    for wire in wires:
        d_wires[wire[0]].append(wire[1])
        d_wires[wire[1]].append(wire[0])
    
    for wire in wires:
        d_wires[wire[0]].remove(wire[1])
        d_wires[wire[1]].remove(wire[0])
        A_group = BFS(d_wires)
        B_group = n - A_group
        answer.append(abs(A_group - B_group))
        d_wires[wire[0]].append(wire[1])
        d_wires[wire[1]].append(wire[0])
    return min(answer)
