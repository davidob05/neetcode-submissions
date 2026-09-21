class Solution:
    def bin_search(self,nums: List[int], target: int, left: int, right: int):
        middle = left + (right-left)//2
        if nums[middle]==target :
            return middle
        elif left>right:
            return -1
        elif nums[middle]>target:
            return self.bin_search(nums,target,left,middle-1)
        else:
            return self.bin_search(nums,target,middle+1,right)

    def search(self, nums: List[int], target: int) -> int:
        return self.bin_search(nums,target,0,len(nums)-1)
    
    
