#User function Template for python3

class Solution:
    def nextPermutation(self, arr):
        # code here
        # length of the array
        n = len(arr)
        
        pivot = -1 # considering worst case i.e, elements in descending order
        
        # finding the index of pivot element
        # comparing a previous element with succesor element - from the rightmost part of array
        # if previous element is smaller that its succesor it will the pivot
        for i in range(n-2, -1, -1):
            if arr[i] < arr[i+1]:
                pivot = i
                break
        
        # if elements in descending order
        # go back to 1st permutation i.e, ascending order
        if pivot == -1:
            arr.reverse()
            return
            
        # check the element just greater than pivot from the rightmost side of array
        # swap it with the pivot element
        for i in range(n-1, pivot, -1):
            if arr[i] > arr[pivot]:
                arr[i], arr[pivot] = arr[pivot], arr[i]
                break
        
        # after swapping
        # elements immediately after pivot elements are sorted in ascending order
        left, right = pivot+1, n-1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
            
            
            
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for i in range(N):
            arr[i] = int(arr[i])

        ob = Solution()
        ob.nextPermutation(arr)
        for i in range(N):
            print(arr[i], end=" ")
        print()

# } Driver Code Ends