'''
1. 문자열 제거 방법
- lower 메소드로 소문자로 통일
- ord()로 영어, 숫자가 아닌 문자 제거
2. 문자열 제거 후 펠린드롬 판별: 투 포인터로 비교. O(N)
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        answer = True
        s = s.lower()
        preprocessed_str = ''
        for i in s:
            if (ord(i) >=97 and ord(i)<=122) or (ord(i)>=48 and ord(i)<=57):#alphanumeric 
                preprocessed_str += i
        for i in range(1,len(preprocessed_str)//2+1):
            if preprocessed_str[i-1] != preprocessed_str[-i]:
                answer = False
                return answer
        return answer
