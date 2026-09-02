class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        counts = {}

        for char in s1:
            if char in counts:
                counts[char]+=1
            else:
                counts[char] = 1
        
        for i in range(0,len(s1)):
            if s2[i] in counts.keys():
                counts[s2[i]]-=1

        if max(counts.values()) == 0:
                return True

        for i in range(0,len(s2)-len(s1)):
            
            
            if s2[i] in counts.keys():
                counts[s2[i]]+=1

            if s2[i+len(s1)] in counts.keys():
                counts[s2[i+len(s1)]] -= 1
            
            if max(counts.values()) == 0:
                return True
        
        return False

