class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l=0
        res=0

        for r, rPrice in enumerate(prices):
            if prices[l] < rPrice:
                profit = rPrice - prices[l]
                res = max(res, profit)
            else:
                l=r
            r+=1
        return res



                
            


            

