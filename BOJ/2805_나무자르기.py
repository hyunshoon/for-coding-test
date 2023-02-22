"""
Goal) 최적의 높이 값(M<= 높이)를 만족하면서 가장 낮은 M 값

Point)
- 찾은 H 값이 M 미터 이상 확보하는 값이면 H 값을 올린다.
"""

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
trees = list(map(int, input().split()))

def check(H):
    sum_woods = M
    for tree in trees:
        if tree > H:
            sum_woods -= (tree-H)
        if sum_woods <=0: #M을 이미 만족
            return True
    return False

def search(start, end):
    if start == end:
        return start
    mid = (start+end+1) // 2
    if check(mid):
        return search(mid, end)
    else:
        return search(start, mid-1)
print(search(0, 1000000000))
