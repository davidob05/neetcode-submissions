class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        required = {}
        for i in range(len(nums)):
            try:
                ind = required[target-nums[i]]
                return [ind,i]
            except KeyError:
                required[nums[i]] = i

