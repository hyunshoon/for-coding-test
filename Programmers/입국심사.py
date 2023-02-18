'''
한 심사대에 한 명

Condition)
n <= 1억
times <= 10만

Goal) 시간. 파라메트릭 서치 search(0, 1억**2)

mid = (start + end+1)//2 로 하면 런타임 에러
'''
def check(result, n, times):
    for i in range(len(times)):
        pass_num = result // times[i]
        n -= pass_num
        if n <=0:
            return True        
    return False    

def search(start, end, n , times):
    if start == end:
        return start
    mid = (start + end)//2 
    if check(mid, n , times):
        return search(start, mid, n , times)
    else:
        return search(mid+1, end, n , times)

def solution(n, times):
    answer = 0
    return search(0, 100000000**2, n , times)
