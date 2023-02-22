"""
Goal) 가장 인접한 두 공유기 사이의 최대 거리

Point)
- 최대거리를 바이너리 서치로 찾는다.
- N개의 집을 순회하며 최대거리를 만족하며 공유기를 배치하는 것에 모두 성공하면 기준치를 높이고 실패하면 낮춘다.
"""

import sys

input = sys.stdin.readline
N, C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))
houses.sort()

def check(distance):
    pre_point = houses[0]
    cnt = 1
    for i in range(1,len(houses)):
        if houses[i] - pre_point >=distance:
            pre_point = houses[i]
            cnt += 1
        if cnt >= C:
            return True
    return False
            
def search(start, end):
    if start == end:
        return start
    mid = (start+end+1) // 2
    if check(mid):
        return search(mid, end) # 성공하면 거리를 늘린다
    else:
        return search(start, mid-1)
print(search(0, 1000000000))
