#1. 현재 위치와 목적지 위치가 같은 원 내부에 있다면 해당 원은 진입/이탈 필요X
#2. 현재 위치와 목적지 위치가 각각 다른 원 내부에 있다면 각 +1
T = int(input())
for t in range(T):
    cnt = 0
    x1, y1, x2, y2 = list(map(int, input().split()))
    planet_n = int(input())
    for p in range(planet_n):
        cx, cy, r = list(map(int, input().split()))
        start_p = (x1 - cx)**2 + (y1 - cy)**2
        end_p = (x2 - cx)**2 + (y2 - cy)**2
        if start_p < r**2:
          if end_p > r**2:#한 가지만 내부에 있는 경우
            cnt+=1
        if end_p < r**2:
          if start_p > r**2:#한 가지만 내부에 있는 경우
            cnt+=1
    print(cnt)
  
