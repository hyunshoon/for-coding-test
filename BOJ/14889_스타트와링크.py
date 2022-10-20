'''
팀을 정하는 프로세스

실패케이스: Sij 선택 시 -> i행, j열에 속한 다른 모든 것 선택 불가능하게 구현. <- 잘못된 풀이. 쌍으로 잡으려고 하니까 문제였음. 

성공케이스
1. combination으로 nCn/2 개의 A 팀 조합 생성
2. A 팀 조합 차집합으로 B 팀 생성

시간복잡도
O(n^3)
최악의 케이스 N=20 일 때, 20C10 * 10 * 5
'''
from itertools import combinations

N = int(input()) 
maps = []
for i in range(N):
    row = list(map(int, input().split(' ')))
    maps.append(row)
for_comb = range(N)

team_A = list(combinations(for_comb, N//2))

# team_A 차집합
team_B = []
for i in range(len(team_A)):
    team_B.append(list(set(for_comb) - set(team_A[i])))

min_value = 100 * 20

for i in range(len(team_A)):#
    score_a = 0
    score_b = 0
    for j in range(N//2):
        for k in range(j+1, N//2):
            score_a += maps[team_A[i][j]][team_A[i][k]]
            score_a += maps[team_A[i][k]][team_A[i][j]]
            score_b += maps[team_B[i][j]][team_B[i][k]]
            score_b += maps[team_B[i][k]][team_B[i][j]]
    min_value = min(abs(score_a - score_b), min_value)
print(min_value)