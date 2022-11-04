'''
N: 입력 받는 단어 개수
K: 가르칠 수 있는 단어 수
단어 길이: 8 ~ 16 
anta, tica 필수
즉, a, c, n, t, i는 필수로 알아야 한다. K < 5 이라면 어떤 단어도 읽지 못한다.
a, c, n, t, i 는 필수로 포함하고 K = K - 5 로 시작

Sol)
1. K - 5 개의 새로운 알파벳 조합을 배웠을 때 모든 단어들을 탐색하며 읽을 수 있는 지 판별
- fail. 21CK-5 의 경우의 수가 너무 많다.

2. 입력 받는 단어 개수 N이 50이하 이므로 여기서 접근

2.1 voca[i]를 배웠을 때, 다음 단어는 어떻게 탐색 하나? voca[i]를 제외한 나머지 모든 경우의수를 계산하면 시간복잡도가 O(N!)이 되므로 불가능

2.2 voca[i]를 배웠을 때, 배운 알파벳을 N 개의 단어리스트에서 제거. 
제거 후 길이가 가장 짧은 단어를 다음으로 배운다.
- 길이가 가장 짧은 단어를 무조건 배우게 되므로 답을 보장하지 않는다.

'''

N, K = map(int, input().split(' '))
K -= 5
answer = 0
voca = []

for i in range(N):
    temp = input().replace('a','').replace('c','').replace('n','').replace('t','').replace('i','')
    temp = list(set(temp))
    voca.append(temp)
voca.sort()
print(voca)

def searching(index, learned):
    learned = set(learned).add(set(voca[index]))

    # for i in range(index, N):
        
        

for i in range(N):
    if len(voca[i]) <= K:
        searching(i)

    