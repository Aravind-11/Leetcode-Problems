class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return
        if len(prices)==1:
            return 0
        n=len(prices)
        max_profit=0
        left=0
        right=1
        while right<n:
            
            profit=prices[right]-prices[left]
            if profit<=0:
                left=right
                
            else:
                max_profit=max(max_profit,profit)
                
            right+=1
        return max_profit
    
        