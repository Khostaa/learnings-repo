# Problem: Smallest Missing Positive
# Problem description:
'''
You are given an integer array arr[]. Your task is to find the smallest positive number missing from the array.

Note: Positive number starts from 1. The array can have negative integers too.
'''
#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        #Your code here
        n = len(arr)
        
        # 
        for i in range(n):
            
            # checking if ith element is within range
            # and swapping the ith elements with its appropriate position
            while 1 <= arr[i] <= n and arr[i] != arr[arr[i]-1]:
                
                # swap arr[i] and (arr[i]-1)th index in arr
                temp = arr[i]
                arr[i] = arr[arr[i]-1]
                arr[temp-1] = temp
         
        # check elements from 1 to n+1
        # if they'are present in apporpiate position, do nothing
        # if missing return them
        for i in range (1, n+1):
            if i != arr[i-1]:
                return i
                
        return n+1
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.missingNumber(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends