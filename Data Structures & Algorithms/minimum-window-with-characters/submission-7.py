class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ""
        
        i = 0
        j = 0

        
        counts = {}
        not_found = len(t)
        best_i = None
        best_j = None
        
        for char in t:
            if char in counts:
                counts[char]+=1 
            else:
                counts[char] = 1 
            

        while j < len(s):
            if s[j] in counts:
                counts[s[j]] -= 1 
                if counts[s[j]] >= 0:
                    not_found -= 1 


            
                if not_found <= 0:
                    if best_i is None:
                        best_i = i 
                        best_j = j 

                    while s[i] not in counts or counts[s[i]]<0: 
                        if s[i] in counts:
                            counts[s[i]]+=1
                        i+=1


                    if j-i < best_j - best_i:
                        best_i = i 
                        best_j = j 
                
            j+=1 

        if best_i is None:
            return ""

        return s[best_i:best_j+1]
                
            
            
            
            

        