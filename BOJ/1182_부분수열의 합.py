#조합 사용
from itertools import combinations

N, S = map(int, input().split())

li = list(map(int, input().split()))
cnt = 0
for i in range(1,len(li)+1):
    comb = list(combinations(li, i))
    for temp in comb:
        if sum(temp) == S:
           cnt +=1
print(cnt)