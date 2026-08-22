class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            if num in freqs.keys():
                freqs[num]+=1
            else:
                freqs[num] = 1
        
        rankings = [[None] for i in range(len(nums)+1)]
        for key,val in freqs.items():
            if rankings[val][0] is None:
                rankings[val][0] = key
            else:
                rankings[val].append(key)

        top_k = []

        for i in reversed(range(len(rankings))):
            if rankings[i][0]is not None:
                for elt in rankings[i]:
                    top_k.append(elt)
                    if len(top_k) == k:
                        return top_k


