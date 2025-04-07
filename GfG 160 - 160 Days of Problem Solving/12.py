# Problem: Maximum Circular Subarray Sum
# Problem description:
'''
Given an array of integers arr[] in a circular fashion. Find the maximum subarray sum that we can get if we assume the array to be circular.
'''

#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    ##Your code here
    n = len(arr)
    cMinSum = 0
    cMaxSum = 0
    totalSum = 0
    minSum = arr[0]
    maxSum = arr[0]
    
    # iterate over the array
    for i in range(n):
        # finding min Sum subarray
        cMinSum = min(cMinSum + arr[i], arr[i])
        minSum = min(minSum,  cMinSum)
        
        # finding max sum subarray
        cMaxSum = max(cMaxSum + arr[i], arr[i])
        maxSum = max(maxSum, cMaxSum)
        
        # summing the whole array
        totalSum += arr[i]
    
    # total Sum = maxSum + minSum => circularSum = totalSum - minSum, here maxSum = circular Sum
    normalSum = maxSum
    circularSum = totalSum - minSum
    
    # if all elements in array negetive i.e minimum subarray then minSum = totalSum
    if minSum == totalSum:
        return normalSum
        
    return max(normalSum, circularSum)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__ == "__main__":
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        print(circularSubarraySum(arr))

        T -= 1
        print("~")

# } Driver Code Ends