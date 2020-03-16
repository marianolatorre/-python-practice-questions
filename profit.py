class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0
        for i in range(1,len(prices)):
            profit += max(prices[i] -prices[i-1], 0)
            print(i, profit)
        return profit

s=Solution()
print(s.maxProfit([1,2,3,4,5]))
for i in range(1,4):
	print(i)