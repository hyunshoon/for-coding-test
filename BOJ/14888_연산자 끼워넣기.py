"""
문제
N개의 수로 이루어진 수열 A1, A2, ..., AN이 주어진다. 또, 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어진다. 연산자는 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)으로만 이루어져 있다.

우리는 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있다. 이때, 주어진 수의 순서를 바꾸면 안 된다.

예를 들어, 6개의 수로 이루어진 수열이 1, 2, 3, 4, 5, 6이고, 주어진 연산자가 덧셈(+) 2개, 뺄셈(-) 1개, 곱셈(×) 1개, 나눗셈(÷) 1개인 경우에는 총 60가지의 식을 만들 수 있다. 예를 들어, 아래와 같은 식을 만들 수 있다.

1+2+3-4×5÷6
1÷2+3+4-5×6
1+2÷3×4-5+6
1÷2×3-4+5+6
식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다. 또, 나눗셈은 정수 나눗셈으로 몫만 취한다. 음수를 양수로 나눌 때는 C++14의 기준을 따른다. 즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다. 이에 따라서, 위의 식 4개의 결과를 계산해보면 아래와 같다.

1+2+3-4×5÷6 = 1
1÷2+3+4-5×6 = 12
1+2÷3×4-5+6 = 5
1÷2×3-4+5+6 = 7
N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.

Point)
- 백트래킹
"""
import sys, copy
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
calculator = list(map(int, input().split()))

max_num = -1000000000
min_num = 1000000000

def back(num_list, depth, cal, value):
    global max_num
    global min_num
    if depth == N:
        max_num = max(max_num, value)
        min_num = min(min_num, value)
    else:# 네 가지 사칙연산 전부 수행
        for i in range(4):
            if cal[i] != 0:
                temp_value = value
                if i == 0:
                    temp_value += num_list[depth]
                elif i == 1:
                    temp_value -= num_list[depth]
                elif i == 2:
                    temp_value *= num_list[depth]
                elif i == 3:
                    if temp_value <0:
                        temp_value *= -1
                        temp_value = (temp_value//num_list[depth]) * -1
                    else:
                        temp_value = temp_value//num_list[depth]
                temp_cal = cal.copy()
                temp_cal[i] -= 1
                back(num_list, depth+1, temp_cal, temp_value)
                
back(num_list, 1, calculator, num_list[0])
print(max_num)
print(min_num)
