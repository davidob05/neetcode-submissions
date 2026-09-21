class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:        
        return self.bin_search(matrix,target,0,(len(matrix[0]))*(len(matrix))-1)  


    def bin_search(self,nums: List[int], target: int, left: int, right: int):
        middle = left + (right-left)//2
        if nums[middle//len(nums[0])][middle%len(nums[0])]==target :
            return True
        elif left>right:
            return False
        elif nums[middle//len(nums[0])][middle%len(nums[0])]>target:
            return self.bin_search(nums,target,left,middle-1)
        else:
            return self.bin_search(nums,target,middle+1,right)