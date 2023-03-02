"""
문제
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

왜 시간 초과 나는지 모르겠음


Point)
- 백트래킹
- 1행에 하나의 퀸만 놓을 수 있다.
- 1행에 열과 대각선을 고려해서 놓을 수 있는 퀸을 열을 반복해서 넣는다.
- visited를 paramaeter로
"""
import sys, copy
input = sys.stdin.readline

N = int(input())
visited = [[False for _ in range(N)] for _ in range(N)]

answer = 0

def is_pass(r,c,visited):
    for pre in range(1,r+1):#is_pass = False 이면 해당 위치에 놓지 못한다.
        left_c = c-pre
        right_c = c+pre
        if visited[pre-1][c] == True:#같은 열
            return False            
        if left_c >=0 and visited[r-pre][left_c] == True:#좌상단 대각선
            return False            
        if right_c <=N-1 and visited[r-pre][right_c] == True:#우상단 대각선
            return False            
    return True

def Back(r, visited):
    global answer
    for c in range(N):
        if is_pass(r,c,visited):
            if r == N-1:
                answer +=1
            else:
                temp_visited = copy.deepcopy(visited)
                temp_visited[r][c] = True
                Back(r+1, temp_visited)
                    
Back(0, visited)
print(answer)

