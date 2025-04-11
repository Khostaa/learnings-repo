# problem: implement Atoi
# problme description:
'''
Given a string s, the objective is to convert it into integer format without utilizing any built-in functions. Refer the below steps to know about atoi() function.

Cases for atoi() conversion:

1. Skip any leading whitespaces.
2. Check for a sign (‘+’ or ‘-‘), default to positive if no sign is present.
3. Read the integer by ignoring leading zeros until a non-digit character is encountered or end of the string is reached. If no digits are present, return 0.
4. If the integer is greater than 2**31 – 1, then return 2**31 – 1 and if the integer is smaller than -2**31, then return -2**31.
'''
#User function template for Python
class Solution:
    def myAtoi(self, s):
        # Code here
        
        # store the sign
        sign = 1 # positive initally
        i = 0 # to traverse the string
        res = 0 # to store the result
        
        # ignore leading whitespaces
        # traverse till sign starts
        while i < len(s) and s[i] == ' ':
            i += 1
            
        # check for sign
        # store the sign of number
        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            i += 1
            
        # taking the number digit by digit
        while i < len(s) and '0' <= s[i] <= '9':
            
            # append current digit to the result
            res = 10 * res  + (ord(s[i]) - ord('0'))
            
            # handling overflow/underflow
            if res > (2**31 - 1):
                return sign * (2 ** 31 - 1) if sign == 1 else -2 ** 31
            i += 1
        
        return res * sign
        

#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.myAtoi(s))
        print("~")

# } Driver Code Ends