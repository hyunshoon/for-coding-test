'''
키가 제일 작은 사람 자리부터 고정
False 로 초기화하고 0 ~ i 까지 순회하며 원소가 False(아직 배정되지 않았으므로 현재 원소 보다 키가 같거나 크다) 일 때 order -= 1 
order == 0 이 되면 그자리에 할당
'''

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key = lambda x: x[0])
        answer = [False] * len(people)
        print(people)


        for i in range(len(people)):
            order = people[i][1]
            for j in range(len(people)):
                if order <= 0:
                    if answer[j] == False: # 0이고 자리가 빈자리라면
                        answer[j] = people[i]
                        break
                    else: # 0이지만 기존에  누군가 있다면
                        continue
                else:# 아직 넣을 차례가 아닌 경우
                    if answer[j] == False:
                        order -=1
                    elif answer[j][0] == people[i][0]: #키가 같다면
                        order -=1
        
        for i in range(len(people)):
            if answer[i] == False:
                answer[i] = people[-1]
        return answer
