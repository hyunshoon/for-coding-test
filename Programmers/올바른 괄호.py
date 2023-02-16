'''
틀리는 조건:
) 가 ( 보다 많아지면 무조건 틀림
최종적으로 괄호 수가 같아야 함.
'''
def solution(s):
    my_dict = {')':0, '(':0}
    for b in s:
        if b == ')':
            my_dict[')'] +=1
        else:
            my_dict['('] +=1
        if my_dict[')'] > my_dict['(']:
            return False
    if my_dict[')'] == my_dict['(']:
        return True
    else: return False
