'''
12P12 는 약 4억 -> 모든 경우의 수를 구할수는 없다.
숫자 네 개로 이루어진 줄의 숫자를 모두 합하면 26 <- 이 조건을 사용하여 경우의 수를 줄여야 한다.

Question)
한 줄이 임의의 조합으로 완성된다면 다른 줄의 완성에 영향을 미치는가? -> 아래 예시를 보면 10 + 7 + x + y =26, x+y = 9가 되야하는게 남아있는 수 중에서 가능한 조합이 없다. 
....x....
.10.8.2.6.
..x...x..
.11.7.5.3.
....y....

Sol) 가장 앞을 가능한 가장 높은 수로 두고 나머지 남은 부분을 백트래킹으로 구현
'''
import sys

magic = []

line1 = [0, 2, 5, 7]
line2 = [0, 3, 6, 10]
line3 = [1, 2, 3, 4]
line4 = [7, 8, 9, 10]
line5 = [1, 5, 8, 11]
line6 = [4, 6, 9, 11]

for _ in range(5):
    magic.append(input().replace(".", ""))

magic_str =''

for m in magic:
    magic_str += m
print(magic_str)


def backtracking():
    pass

