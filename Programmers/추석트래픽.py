#끝나는 시간을 기준으로 해야하는데 시작시간을 기준으로해서 계속 틀림
#끝나는 시간 오름차순으로 정렬되어있기 때문에 끝나는 시간 기준으로 다음차례부터 순회.

def solution(lines):
    def str_to_millesecond(lines):
        li = []# 끝나는 시간, 소요시간, 시작시간
        for line in lines:
            li.append((line[11:].replace('s', '').replace(':', '').split(' ')))
        for i in range(len(li)):#시간을 ms단위로 바꾸기
            time = 0
            time += int(li[i][0][:2]) * 3600*1000
            time += int(li[i][0][2:4]) * 60*1000
            time += int(li[i][0][4:6]) * 1000
            time += int(li[i][0][7:])
            li[i][0] = time #끝나는 시간
            li[i][1] = int(float(li[i][1])*1000)#소요시간
        for i in range(len(li)):#시작 시간 계산
            end_time = li[i][0]
            start_time = end_time - li[i][1] +1 #시작시간
            li[i] = [start_time, end_time] # 시작시간, 끝나는시간
        return li
    li = str_to_millesecond(lines)    
    answer = 0
    for i in range(len(li)):
        end = li[i][1]
        cnt = 0
        for j in range(i,len(li)):
            next_start_time = li[j][0]
            if end > next_start_time - 1000:
                cnt+=1
        answer = max(answer, cnt)
            
    return answer