#팰린드롬을 어떻게 판별하는가?
#문자열 길이:n
#1. (0, n-1), (1, n-2)와 비교해서 하나라도 틀리면 펠린드롬이 아닌 부분문자열이다.
#2. 모두 같으면 펠린드롬이다.
#3. 펠린드롬인 경우 문자열이 모두 같은 경우를 제외하고 n-1이 답이다.
def check():
    string = input()
    n = len(string)
    result = -1
    for i in range(n//2):
        if string[i] != string[n-i-1]:#펠린드롬이 아니다 판별
            result = n
            return result
    for i in range(1,n):
        if string[0] != string[i]:
            result = n-1
            return result
    return result
print(check())