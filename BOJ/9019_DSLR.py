#메모리초과 왜 뜸?
#메모리 초과가 뜨는 이유는 이미 답이 아니라고 판별난 경우도 경우의 수를 증폭시켜서 그렇다.
#hist list를 만들어서 포함된 것은 넣지 않는다. -> 딕셔너리로 변경해야한다. 딕셔너리는 특정 값 탐색시 O(1)이지만 list는 O(n)이다.
#L, R의 경우가 잘못되있다.
from collections import deque
T = int(input())
def D(cur, target, log):
    cur *= 2
    if cur>9999:
        cur %= 10000
    return cur, target, log + 'D'
    
def S(cur, target, log):
    if cur == 0:
        cur = 9999
    else:
        cur -= 1
    return cur, target, log + 'S'
    
def L(cur, target, log):
    cur = (cur%1000)*10 + cur//1000
    return cur, target, log + 'L'


def R(cur, target, log):
    cur = (cur%10)*1000 + (cur//10)
    return cur, target, log + 'R'

def bfs(cur, target):
    queue = deque()
    queue.append((cur, target, ''))
    dict_hist = {}
    
    while queue:
        cur, target, log = queue.popleft()
        if cur == target:
            return log
        else:
            temp_li = []
            temp_li.append(D(cur, target, log))
            temp_li.append(S(cur, target, log))
            temp_li.append(L(cur, target, log))
            temp_li.append(R(cur, target, log))
            for temp in temp_li:
                if temp[0] not in dict_hist and temp[0]<10000 and temp[0]>=0:
                    queue.append(temp)
                    dict_hist[temp[0]] = temp[0]
for _ in range(T):
    temp = list(map(int, input().split(' ')))
    print(bfs(temp[0], temp[1]))