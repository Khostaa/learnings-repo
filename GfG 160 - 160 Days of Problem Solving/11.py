# Problem: Maximum Product subarray
# Problem description:
'''
Given an array arr[] that contains positive and negative integers (may contain 0 as well). Find the maximum product that we can get in a subarray of arr[].

Note: It is guaranteed that the output fits in a 32-bit integer.
'''
#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		# code here
        n = len(arr)
        
        # max product ending at current index
        lMax = arr[0]
        
        # min product ending at current index
        lMin = arr[0]
        
        # initialize overall maximum product
        mProd = arr[0]
        
        for i in range(1, n):
            temp = max(arr[i], arr[i]*lMax, arr[i]*lMin)
            
            lMin = min(arr[i], arr[i]*lMax, arr[i]*lMin)
            
            lMax = temp
            
            mProd = max(mProd, lMax)
        return mProd
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends