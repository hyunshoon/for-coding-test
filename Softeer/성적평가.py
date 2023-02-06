'''
문제
현주는 N명의 인원이 참여하는 프로그래밍 스터디 그룹을 이끌고 있다.

현주는 스터디를 위해 대회를 세 개 개최하였고, 모든 구성원이 각 대회에 참여하였다. 참가자는 각 대회에서 0 이상 1,000 이하의 정수인 점수를 얻는다. 한 대회에서 둘 이상의 참가자가 동점이 나오는 경우도 있을 수 있다.

현주는 각 대회별 등수 및 최종 등수를 매기고 싶다. 등수는 가장 점수가 높은 사람부터 1등, 2등, ···, N등의 순서대로 붙는다. 만일 동점이 있을 경우 가능한 높은 (등수의 수가 작은) 등수를 부여한다. 즉, 점수가 내림차순으로 10,7,6,6,4의 순서일 경우, 6점을 받은 두 사람은 공동 3등이 되고, 그 다음 순서인 4점을 받은 사람은 5등이 된다. 이 규칙을 다르게 표현하면 다음과 같다: 각 사람마다 “나보다 점수가 큰 사람”의 수를 세어 1을 더한 것이 자신의 등수가 된다. 대회별 등수는 각 대회에서 얻은 점수를 기준으로 하며 최종 등수는 세 대회의 점수의 합을 기준으로 한다.

각 참가자의 대회별 등수 및 최종 등수를 출력하는 프로그램을 작성하시오.

제약조건
3 ≤ N ≤ 100,000

입력형식
첫째 줄에 참가자의 수를 나타내는 정수 N이 주어진다.
이어 세 개의 줄에 각 대회의 결과를 나타내는 N개의 정수가 주어진다. 이중 i번째 정수는 그 대회에서 i번째 사람이 얻은 점수를 의미한다.

출력형식
첫 세 개의 줄에는 각 참가자의 대회별 등수를 출력한다. 즉 이중 c번째 줄의 i번째 정수는 c번째 대회에서의 i번째 사람의 등수를 의미한다.
이어 새로운 줄에 같은 형식으로 각 참가자의 최종 등수를 출력한다.
----------------------------------
Point
1. O(NlogN)이내로 문제 해결해야함
2. 입력을 쭉 받고 정렬하는 방법 vs 입력을 받으며 정렬 하는 방법. -> 후자 heapq로 구현하여 pop하며 공동 등수를 가려내야 한다.

Caution
입력 받을 때 i번째 정수를 같이 입력해야 하므로 heap을 2차원 배열로 입력한다.
최대 힙으로 구현해야 공동 등수를 가리기 편하다. 값이 달라질 때 그 값의 등수를 바로 정할 수 있기 때문.

'''
import sys
import heapq

N = int(input())
first_h = []
sec_h = []
third_h = []
total_h = []
first= list(map(int, sys.stdin.readline().split(' ')))
sec= list(map(int, sys.stdin.readline().split(' ')))
third = list(map(int, sys.stdin.readline().split(' ')))
for i in range(N):
    heapq.heappush(first_h, (-first[i], i))
    heapq.heappush(sec_h, (-sec[i], i))
    heapq.heappush(third_h, (-third[i], i))
    heapq.heappush(total_h, (-first[i]-sec[i]-third[i], i))

first_r = [0 for _ in range(N)]
sec_r = [0 for _ in range(N)]
third_r = [0 for _ in range(N)]
total_r = [0 for _ in range(N)]

first_pre,i1_pre = heapq.heappop(first_h)
sec_pre,i2_pre = heapq.heappop(sec_h)
third_pre,i3_pre = heapq.heappop(third_h)
total_pre,i4_pre = heapq.heappop(total_h)

first_r[i1_pre] = 1
sec_r[i2_pre] = 1
third_r[i3_pre] = 1
total_r[i4_pre] = 1
for i in range(2,N+1):#출력
    first_cur, i1_cur = heapq.heappop(first_h)
    sec_cur, i2_cur = heapq.heappop(sec_h)
    third_cur, i3_cur = heapq.heappop(third_h)
    total_cur, i4_cur = heapq.heappop(total_h)
    if first_cur == first_pre:
        first_r[i1_cur] = first_r[i1_pre]#같은 등수
    else:
        first_r[i1_cur] = i
    if sec_cur == sec_pre:
        sec_r[i2_cur] = sec_r[i2_pre]#같은 등수
    else:
        sec_r[i2_cur] = i
    if third_cur == third_pre:
        third_r[i3_cur] = third_r[i3_pre]#같은 등수
    else:
        third_r[i3_cur] = i
    if total_cur == total_pre:
        total_r[i4_cur] = total_r[i4_pre]#같은 등수
    else:
        total_r[i4_cur] = i
    
    first_pre = first_cur
    sec_pre = sec_cur
    third_pre = third_cur
    total_pre = total_cur
    i1_pre = i1_cur
    i2_pre = i2_cur
    i3_pre = i3_cur
    i4_pre = i4_cur
print(" ".join(map(str,first_r)))
print(" ".join(map(str,sec_r)))
print(" ".join(map(str,third_r)))
print(" ".join(map(str,total_r)))
