#sorted된 상태에서 나누는 구간만 정하면 된다.
#어떻게 k개로 나누지?

N, k = map(int, input().split(' '))
tall = list(map(int, input().split(' ')))

diff = [tall[i+1] - tall[i] for i in range(N-1)]
diff.sort()

print(sum(diff[:N-k]))

'''
N명의 학생들을 K그룹으로 나눈다는 것은 K개의 키 차이를 무시할 수 있다는 것.
K그룹으로 나누는 칸막이를 가장 차이가 많이나는 N-K

아쉬운점: '키'라는 각 원소에 집중하지 않고 목적 값인 'cost'에 집중 하면 좋았을 것. 
'''