'''
유지할 치킨집 고르는 프로세스.
첫 번째 방법: 1, 2, ... , a 개 폐점 시킬때 마다 그리디로 폐점시킬 치킨 집 선정. 최적해 보장 X 이므로 실패
두 번째 방법: 조합을 이용한 완전탐색

치킨집 개수: a, 유지시킬 치킨 집 개수: m
process
1. m개의 치킨집을 유지시킴. aCm 개의 조합을 뽑고 최소값 선정하면 답.
2. 1(집)과 2(치킨집)의 위치를 가진 리스트 생성
3. combination으로 선별된 치킨집 리스트중 집에서 가장 가까운 치킨거리를 찾는다. 3번을  집의 개수만큼 반복
4. 3번 값을 합쳐서 result 리스트에 저장.

for 조합으로 뽑은 치킨집 리스트
    for 집 개수 (모든 집의 치킨거리를 구해야 함)
        for 치킨거리 계산 (해당 집에서 가장 가까운 치킨집 찾음)

시간복잡도: O(n^3). n^3는 대부분 실패하지만
aCm * 2N * M 으로 최대값을 계산했을 때 N:50, M:13, a:13
최악의 케이스 100 * 13 * 13C6(1716)이므로 시간제한 1초안에 충분히 가능하다.
'''
from itertools import combinations

N, M = map(int, input().split())
house = []
chiken = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            house.append((i,j))
        elif row[j] == 2:
            chiken.append((i,j))

live = list(combinations(chiken, M))
result = []

for i in range(len(live)):#combinations로 뽑은 
    sum_distance = 0
    for h in range(len(house)):#집 개수. 모든 집의 치킨거리 최솟값을 구해야 한다.
        min_value = 100
        for j in range(M):
            temp = abs(live[i][j][0] - house[h][0]) + abs(live[i][j][1] - house[h][1])
            min_value = min(min_value, temp)
        sum_distance += min_value
    result.append(sum_distance)
print(min(result))
