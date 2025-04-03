# Problem: Stock Buy and Sell, Multiple transaction allowed
# Problem description:
# The cost of stock on each day is given in an array price[]. Each day you may decide to either buy or sell the stock i at price[i], you can even buy and sell the stock on the same day. Find the maximum profit that you can get.
#Note: A stock can only be sold if it has been bought previously and multiple stocks cannot be held on any given day.

from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        res = 0
        n = len(prices) - 1
        for i in range(1, n+1):
            if prices[i] > prices[i-1]:
                res = res + prices[i] - prices[i-1]
                
        return res
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.maximumProfit(arr)
        print(res)
        print("~")

# } Driver Code Ends