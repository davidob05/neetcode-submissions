class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        counts = {}
        n1 = len(s1)

        for char in s1:
            if char in counts:
                counts[char]+=1
            else:
                counts[char] = 1
        
        for i in range(0,n1):
            if s2[i] in counts.keys():
                counts[s2[i]]-=1

        not_matched = 0

        for count in counts.values():
            if count!=0:
                not_matched+=1

        if not_matched == 0:
            return True

        for i in range(0,len(s2)-n1):
            
            if s2[i] in counts.keys():
                if counts[s2[i]] == 0:
                    not_matched += 1
                elif counts[s2[i]] == -1:
                    not_matched -= 1
                counts[s2[i]]+=1
                

            if s2[i+len(s1)] in counts.keys():
                counts[s2[i+n1]] -= 1
                if counts[s2[i+n1]] == 0:
                    not_matched -= 1
                elif counts[s2[i+n1]] == -1:
                    not_matched += 1

            
            if not_matched == 0:
                return True
        
        return False

