#point1: 강의가 끝난 강의실에는 새로운 강의를 어디에 추가하는지는 상관없다.
#point2: 강의가 끝나는 시간을 강의실 리스트로 생성. 현재 강의실을 배정하는 강의를 넣을 수 있다면 원소를 대체해서 넣고, 그렇지 못하다면 새롭게 원소 추가. 원소의 개수는 강의실 개수가 됌.

#lec_li를 start_time기준으로 sort하면 맞고 end_time기준으로 sort하면 틀린다.
#이유 생각
import heapq
N = int(input())
lec_li = []
for _ in range(N):
    start, end = list(map(int, input().split(' ')))
    lec_li.append((start, end))

lec_li = sorted(lec_li, key = lambda x: x[0])
#lec_li[i][0]: start time
#lec_li[i][1]: end time
room_heap = [lec_li[0][1]]
for lec in lec_li[1:]:
    # print(lec, room_heap)
    start_time = lec[0]
    end_time = lec[1]
    
    last_time = heapq.heappop(room_heap)#현재 우선순위큐에서 끝나느 시간이 가장 빠른 시간 추출
    if last_time <= start_time:# 새 강의 시작시간이 강의실에서 이전 강의 끝나느시간보다 크거나 같아야함.
        heapq.heappush(room_heap,end_time)
    else:#강의실을 추가
        heapq.heappush(room_heap, end_time)
        heapq.heappush(room_heap, last_time)
        
print(len(room_heap))

