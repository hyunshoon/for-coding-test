from collections import defaultdict
def DFS(t_dict, answer, depth, complete):
    if depth == complete:
        return answer
    else:
        next_port = t_dict[answer[-1]]# 한 출발지에서 도착지가 여러개
        next_port.sort()
        
        for n in next_port:
            tmp = answer[:]
            tmp.append(n)
            t_dict[answer[-1]].remove(n)
            result = DFS(t_dict, tmp, depth+1, complete)
            t_dict[answer[-1]].append(n)
            t_dict[answer[-1]].sort()
            if result:
                return result

def solution(tickets):
    tickets_dict = defaultdict(list)
    for t in tickets:
        tickets_dict[t[0]].append(t[1]) #출발지에 
    result = DFS(tickets_dict, ["ICN"], 1, len(tickets)+1)
    return result

