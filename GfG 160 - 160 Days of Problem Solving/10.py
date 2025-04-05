# Problem: Kadane's Algorithm

# Problem description:
#Given an integer array arr[]. You need to find the maximum sum of a subarray.
class Solution:
    def maxSubArraySum(self, arr):
        # Your code here
        n = len(arr)
        res = arr[0]
        max_end = arr[0]
        
        for i in range(1, n):
            # finding the maximum sum upto current element
            max_end = max(max_end + arr[i], arr[i])
            
            # update the result
            res = max(res, max_end)
            
        return res
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends