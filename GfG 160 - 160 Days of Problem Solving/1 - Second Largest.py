#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        if len(arr) < 2:
            return -1
     
        fmax, smax = float('-inf'), float('-inf')
        for num in arr:
            if num > fmax:
                smax = fmax
                fmax = num
            elif fmax > num > smax:
                smax = num
        
        if smax == float('-inf'):
            return -1
        return smax
#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends