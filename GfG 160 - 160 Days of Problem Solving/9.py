#Problem: Minimize the Heights II
#Problem description:
'''Given an array arr[] denoting heights of N towers and a positive integer K.

For each tower, you must perform exactly one of the following operations exactly once.

- Increase the height of the tower by K
- Decrease the height of the tower by K
Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

You can find a slight modification of the problem here.
Note: It is compulsory to increase or decrease the height by K for each tower. After the operation, the resultant array should not contain any negative integers.
'''

# Approach:

'''
The idea is to sort the array and check the maximum height difference at each index by increasing the height of towers up 
to that index and decreasing the height of towers beyond that index.

For any index i, if we add k to all heights in subarray arr[0...i-1] and subtract k from all heights in subarray arr[i...n-1], 
then we know that 
smallest height = min(arr[0]+k, arr[i]-k) 
and 
tallest height = max(arr[i-1]+k, arr[n-1]-k). 
So, the smallest difference between tallest height and smallest height over all indices will be the result.

We can see that for any index i, the smallest height depends on arr[0] and arr[i] and the tallest height depends on arr[i - 1] 
and arr[n - 1], so instead of modifying the subarrays arr[0...i-1] and arr[i...n-1], we can simply modify 
arr[0], arr[i - 1], arr[i] and arr[n - 1] to get the smallest difference between heights.
'''
#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        # code here
        n = len(arr)
        # sorting the array
        arr.sort()
        
        # initially maximum differences
        res = arr[n-1] - arr[0]
        
        for i in range(1, n):
            if arr[i] - k < 0:
                continue
            else:
                # get the minimum height
                minHeight = min(arr[0]+k, arr[i] - k)
                # get the maximum height
                maxHeight = max(arr[i-1]+k, arr[n-1]-k)
                # update result
                res = min(res, maxHeight - minHeight)
                
        return res
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, k)
        print(ans)
        print("~")
        tc -= 1

# } Driver Code Ends