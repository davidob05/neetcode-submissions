class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        counts = [0]*26

        for char in s1:
            counts[ord(char)-97]+=1
        
        for i in range(0,len(s1)):
            counts[ord(s2[i])-97]-=1

        not_matched = 0

        for count in counts:
            if count!=0:
                not_matched+=1

        if not_matched == 0:
            return True

        for i in range(0,len(s2)-len(s1)):
            
            if counts[ord(s2[i])-97] == 0:
                not_matched += 1
            elif counts[ord(s2[i])-97] == -1:
                not_matched -= 1
            counts[ord(s2[i])-97]+=1
                
            counts[ord(s2[i+len(s1)])-97] -= 1
            if counts[ord(s2[i+len(s1)])-97] == 0:
                not_matched -= 1
            elif counts[ord(s2[i+len(s1)])-97] == -1:
                not_matched += 1

            
            if not_matched == 0:
                return True
        
        return False

