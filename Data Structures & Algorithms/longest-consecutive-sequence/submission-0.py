class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums= set(nums)
        max_seq = 0
        for num in nums:
            if num-1 not in nums:
                seq = 1
                i=1
                while num+i in nums:
                    seq+=1
                    i+=1
                if seq>max_seq:
                    max_seq = seq
        return max_seq
                


