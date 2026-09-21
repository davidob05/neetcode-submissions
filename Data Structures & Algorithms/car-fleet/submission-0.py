class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def argsort(l):
            return sorted(range(len(l)), key=l.__getitem__)[::-1]

        sorted_indices = argsort(position)
        fleets = 0
        prev_time = None


        for i in range(len(sorted_indices)):
            time = (target - position[sorted_indices[i]])/speed[sorted_indices[i]]
            if prev_time == None or prev_time<time:
                fleets+=1
                prev_time = time

        return fleets
