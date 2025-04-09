# Problem - Anagram Strings

# problem description:
'''
Given two strings s1 and s2 consisting of lowercase characters. The task is to check whether two given strings are an anagram of each other or not. An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, "act" and "tac" are an anagram of each other. Strings s1 and s2 can only contain lowercase alphabets.

Note: You can assume both the strings s1 & s2 are non-empty.
'''

#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        #code here
        # max characters in lower case is 26
        MAX_CHAR = 26
        
        # list to keep track of frequency of each character
        freq = [0] * MAX_CHAR
        
        # for each character in string, s1 increase its frequency by 1 at index ord(ch) - ord('a')
        for ch in s1:
            freq[ord(ch) - ord('a')] += 1
        
        # if that char, ch is present in s2 then decrease the frequncy by 1 at index ord(ch) - ord('a')
        for ch in s2:
            freq[ord(ch) - ord('a')] -= 1
          
        # if all values in frequency are not zero, then not anagrams  
        for count in freq:
            if count!= 0:
                return False
        # else, anagrams
        return True
            
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a = input().strip()
        b = input().strip()
        if (Solution().areAnagrams(a, b)):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends