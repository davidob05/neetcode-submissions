class Solution:


    def makeKey(self, stri: str):
        counts = [0]*26

        for char in stri:
            counts[ord(char) - 97] += 1
        
        return tuple(counts)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups_dict = {}
        for i in range(len(strs)):
            key = self.makeKey(strs[i])
            if key in groups_dict.keys():
                groups_dict[key].append(strs[i])
            else:
                groups_dict[key] = [strs[i]]
        return [i for i in groups_dict.values()]
            




        