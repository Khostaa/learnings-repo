
# Problem: Non Repeating Character
#problem description:
'''
Given a string s consisting of lowercase English Letters. Return the first non-repeating character in s.
If there is no non-repeating character, return '$'.
Note: When you return '$' driver code will output -1.
'''
class Solution:
    def nonRepeatingChar(self,s):
        #code here
        MAX_CHAR = 26
        
        freq = [0] * MAX_CHAR
        for ch in s:
            freq[ord(ch) - ord('a')]+= 1
        
        for ch in s:
            if freq[ord(ch) - ord('a')] == 1:
                return ch
        
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        ans = obj.nonRepeatingChar(s)
        if (ans != '$'):
            print(ans)
        else:
            print(-1)

        print("~")

# } Driver Code Ends