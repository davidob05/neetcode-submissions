class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_nums = []
        max_i = 0
        max_num = -10001
        for i in range(k):
            if nums[i]>=max_num:
                max_num = nums[i]
                max_i = i
        max_nums.append(max_num)
        
        for i in range(len(nums) - k):
            if max_num <= nums[i+k]:
                max_nums.append(nums[i+k])
                max_num = nums[i+k]
                max_i = i+k
            elif max_i<=i:
                max_i = i+1
                max_num = nums[i+1]
                for j in range(1,k+1):
                    if nums[j+i]>=max_num:
                        max_num = nums[i+j]
                        max_i = i+j
                max_nums.append(max_num)
            else:
                max_nums.append(max_num)

        return max_nums

