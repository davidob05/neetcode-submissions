class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper = max(piles)
        lower = 1
        found = False
        while not found:
            middle = lower + (upper-lower)//2
            if self.has_enough_time(piles,middle,h):
                if lower == middle:
                    return middle
                upper = middle
            elif not self.has_enough_time(piles,middle,h):
                lower = middle+1

    def has_enough_time(self,piles,k,h):
        tot = 0
        for pile in piles:
            tot+=math.ceil(pile/k)
        return tot<=h
            
            

        