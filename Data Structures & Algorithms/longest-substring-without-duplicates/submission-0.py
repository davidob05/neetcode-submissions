class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        max_len = 1
        unique = {s[0]:0}
        i,j = 0,1
        while j < len(s):
            if s[j] not in unique or unique[s[j]]<i:
                unique[s[j]] = j
                if max_len < j-i+1:
                    max_len = j-i+1
           
            else:
                i=unique[s[j]] + 1

            unique[s[j]] = j

            j+=1
        return max_len