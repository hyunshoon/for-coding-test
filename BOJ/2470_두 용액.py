"""
Goal) 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 혼합을 하는 것

Point)
- O(N), O(NlogN)
- 특정 값을 먼저 선택하고 최대한 0과 가까운 조합의 수를 선택하는 것 -> O(N^2)
- 파라메트릭 서치로 시간 복잡도 해결
- 특정 값을 먼저 선택하고 O(N) 바이너리 서치로 해당 값과 가장 가까운 값 서칭 O(logN) -> O(NlogN)
"""
import sys
input = sys.stdin.readline
N = int(input())
liquids = list(map(int, input().split()))
liquids.sort()
set_liq = set(liquids)

def check(target):
    for liq in liquids:
        first = liq
        if target - first in set_liq:
            return True
    return False

def search(first, start, end):
    if start == end:
        return start
    mid = (start+end)//2
    if check(mid):
        return search(start, mid)
    else:
        return search(mid+1, end)
    
for liq in liquids:
    first = liq
    sec = -first
    search(first, -1000000000,1000000000)



