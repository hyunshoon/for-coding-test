'''
Point
사전 순서를 정립 방식
1. A +1 == AA
2. AAAAA + 1 == AAAAE
3. AAAAU +1 == AAAE

DFS로 푼다.
딕셔너리 리스트에 A 추가 -> DFS -> AA추가 -> DFS ->... -> AAAAA 에서 끝. 
'''
def DFS(dictionary, cur_words):
    vowel = ['A', 'E', 'I', 'O', 'U']
    if len(cur_words) < 5:#추가 가능
        for v in vowel:
            temp = cur_words[:]
            temp += v
            dictionary.append(temp)
            DFS(dictionary, temp)
            
def solution(word):
    answer = 0
    dictionary = []
    DFS(dictionary, '')
    for i in range(len(dictionary)):
        if dictionary[i] == word:
            return i+1
