class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        all_comb = []
        answer = []
        def DFS(li):
            if sum(li) > target:
                return
            elif sum(li) == target:
                answer.append(sorted(li))
            else:
                for c in candidates:
                    temp = [c]
                    temp.extend(li)
                    DFS(temp)
        DFS([])
        
        final_answer = []
        for a in answer:
            if a not in final_answer:
                final_answer.append(a)
        return final_answer

