'''
1. 사는 시기를 어떻게 정하는지?
2. 파는 시기를 어떻게 정하는지?

살 때 조건: price[i] < price[i+1] 이면 산다. 다음날보다 싸니까
팔 때 조건: price[i] > price[i+1] 이면 판다. 다음날 다시사면 더 이득이니까
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        position = 0# position: 0 <- buy, 1 <- sell
        share = 0
        for i in range(len(prices)-1):
            if position == 0:
                if prices[i] < prices[i+1]:
                    share = prices[i]
                    position = 1
            else:# 팔 때 
                if prices[i] > prices[i+1]:
                    profit += (prices[i] - share)
                    position = 0
     
        if position == 1:#  아직 못 팔았을 때
            profit += (prices[-1] - share)

        return profit
