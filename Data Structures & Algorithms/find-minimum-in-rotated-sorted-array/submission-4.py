class Solution:
    def findMin(self, nums: List[int]) -> int:
        upper = len(nums)-1
        lower = 0

        while True:
            middle = lower + (upper-lower)//2
            if middle==lower:
                return min(nums[lower],nums[upper])
            elif nums[middle]>nums[upper]:
                lower = middle
            elif nums[lower]>nums[middle]:
                upper = middle
            else:
                return nums[lower]

            
            