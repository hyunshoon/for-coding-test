class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}

        for num in nums:
            if num in table.keys():
                table[num] += 1
            else:
                table[num] = 0
        sorted_list = sorted(table.items(), key=lambda x:x[1], reverse=True)
        answer = []
        for i in range(k):
            answer.append(sorted_list[i][0])
        return answer
