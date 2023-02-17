'''
https://www.youtube.com/watch?v=-xp1Pc6_lIc 를 참고
'''

import sys
input = sys.stdin.readline

def check(target):
    temp = [0] * N
    temp[0] = C[0]
    for i in range(N-1):
        if temp[i] >= target:
            temp[i+1] = C[i+1] + D[i]
        elif temp[i] + D[i] >= target:
            temp[i+1] = C[i+1] + (temp[i] + D[i] - target)
        else:
            return False
    if temp[N-1] >= target:
        return True
    else:
        False

def Search(start, end):
    if start == end:
        return start
    mid = (start + end)//2 + 1
    if check(mid):
        return Search(mid, end)
    else:
        return Search(start, mid-1)

N, T = map(int, input().split())
for _ in range(T):
    inp = list(map(int, input().split()))
    C = []
    D = []
    for i in range(N - 1):
        C.append(inp[2*i])
        D.append(inp[2*i + 1])
    
    C.append(inp[2 * (N - 1)])

    print(Search(0, 2*10**12))
