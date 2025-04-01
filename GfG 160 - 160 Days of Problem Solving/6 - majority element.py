class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        n = len(arr)
        counted = []
        visited = {}

        # count the frequency of each element in the array
        # and store it in a dictionary
        for i in range(n):
            if arr[i] not in visited.keys():
                count = 1
                visited[arr[i]] = count
                
            elif arr[i] in visited.keys():
                count+=1
                visited[arr[i]] += 1
        # sort the dictionary based on the frequency of elements
        visited = dict(sorted(visited.items(), key=lambda item: item[1], reverse=False))
        threshold = n//3
        
        # check if the frequency of each element is greater than n/3
        # if yes, add it to the counted list
        counted = [key for key, value in visited.items() if value > threshold]
        # arrange the counted list in ascending order
        # as the problem statement requires the majority elements to be in ascending order
        counted.sort()
        return counted           

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends