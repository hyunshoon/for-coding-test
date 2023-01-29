'''
1. 현재 단어에서 변환할 수 있는 모든 단어로 변환

주의사항
1. 이미 변환한 단어로는 변환X -> 중복 제거를 위해
'''
from collections import deque

def BFS(begin, target, words):
    queue = deque()
    check_list = []
    queue.append((begin, 0))
    while queue:
        cur_word, cnt = queue.popleft()
        for next_word in words:
            if next_word in check_list:continue # 이미 변환 했던 단어
            if next_word == cur_word:continue # 자기 자신
            
            diff_str_cnt = 0
            for i in range(len(next_word)):
                if next_word[i] != cur_word[i]:
                    diff_str_cnt +=1
                    if diff_str_cnt >1:
                        break
            if diff_str_cnt == 1:
                if next_word == target:
                    return cnt+1
                queue.append((next_word, cnt+1))
                check_list.append(next_word)
    return 0
        
def solution(begin, target, words):
    answer = BFS(begin, target, words)
    return answer
