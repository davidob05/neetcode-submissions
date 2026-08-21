class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False

        occurrences_s = {}
        occurrences_t = {}
        for i in range(len(s)):
            if s[i] in occurrences_s.keys():
                occurrences_s[s[i]] = occurrences_s[s[i]]+1
            else:
                occurrences_s[s[i]] = 1
            if t[i] in occurrences_t.keys():
                occurrences_t[t[i]] = occurrences_t[t[i]]+1
            else:
                occurrences_t[t[i]] = 1

        for key,val in occurrences_s.items():
            if key not in occurrences_t.keys():
                return False
            elif val != occurrences_t[key]:
                return False

        return True