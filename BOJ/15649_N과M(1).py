from itertools import permutations

N, M = map(int, input().split(' '))

seq = list(range(1, N+1))

result = list(permutations(seq, M))

for r in result:
    temp = list(map(str, r))
    print(' '.join(temp))