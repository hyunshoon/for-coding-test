class Solution(object):

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        answer = []
        table = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        if digits=="":
            return []
        def DFS(index, path):
            if len(path) == len(digits):
                answer.append(path)
                return
            else:
                for s in table[digits[index]]:
                    DFS(index+1, path+s)
        DFS(0, "")
        return answer



