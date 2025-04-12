# Problem: Add Binary Strings
# Problem Description:
'''
Given two binary strings s1 and s2 consisting of only 0s and 1s. Find the resultant string after adding the two Binary Strings.
Note: The input strings may contain leading zeros but the output string should not have any leading zeros.
'''
#User function Template for python3
class Solution:
    
    def trimLeadingZeros(self, s):
        first = s.find('1')
        return s[first:] if first != -1 else "0"
        
    def addBinary(self, s1, s2):
        # code here
        # trim leading zeros
        s1 = self.trimLeadingZeros(s1)
        s2 = self.trimLeadingZeros(s2)
        
        # get length of strings
        m = len(s1)
        n = len(s2)
        
        # Swap strings if s1 is of smaller length
        if m < n:
            s1, s2 = s2, s1
            m, n = n, m
        
        j = n - 1  # for last digit of s2
        carry = 0
        res = []
        
        # let's add from the end
        for i in range(m - 1, -1, -1):
            
            # Current bit of s1
            bit1 = int(s1[i])
            # to track bit's sum
            bitSum = bit1 + carry
            
            # for s2
            if j >= 0:
                bit2 = int(s2[j])
                bitSum += bit2
                j -= 1
            
            # rectify to binary addition
            # take remainder
            bit = bitSum % 2
            carry = bitSum // 2  # Floor division for carry bit
            
            # update the res
            res.append(str(bit))
                
        # if any carry left at the end
        if carry > 0:
            res.append('1')
            
        # since Sum is reveresed, return its reverse to get actual sum
        return ''.join(res[::-1])

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        a = input().strip()
        b = input().strip()
        ob = Solution()
        answer = ob.addBinary(a, b)

        print(answer)
        print("~")

# } Driver Code Ends