class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        n = len(s) - 1
        i = 0
        while n > i:
            while not s[i].isalnum() and i<len(s)-1:
                i+=1
        
            while not s[n].isalnum() and n>0:
                n-=1
                
            if s[i] != s[n] and s[i].isalnum() and s[n].isalnum():
                return False
            n-=1
            i+=1
        return True