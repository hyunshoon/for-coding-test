'''
Point)
--------
실패한 방법
1. 현재 수에서 하나 제거했을 때 가장 큰 수 제거
2. 앞에서부터 제거하면서 다음 값이 이전 값 보다 커지면 이전 값을 제거하는게 최적 조건
3. 이전 값 제거 후 다시 처음부터 비교해야한다. 그렇지 않으면 41753 같은 경우 1만 제거하고 4는 제거하지 못한다.
4. 3번의 문제점은 54321 같은 경우 O(n^2)이 되어 시간초과가 되는 문제가 있다.
----------- 
O(N)만으로 가능하려면 순회하면서 바로 결정을 해야한다.

Condition)
n == 백만
O(n^2) 시간 복잡도를 가지면 안된다.
O(n) 혹은 O(nlogn)

Example) 남은 k 값 처리 해야하는 이유
number:21, k:1
stack = [2, 1]
'''
def solution(number, k):
    number = [int(n) for n in number]
    stack = []
    for i in range(len(number)):
        if not stack or k<=0:#스택이 비어있는 경우와 더 이상 제거하지 못하는 경우
            stack.append(number[i])
            continue
        while stack and stack[-1] <number[i] and k > 0:
            stack.pop()
            k-=1
        stack.append(number[i])
    while k>0:
        stack.pop()
        k-=1
    answer = "".join(map(str, stack))
    return answer
