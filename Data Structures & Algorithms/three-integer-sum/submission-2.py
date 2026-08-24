class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for pair in self.twoSum(nums, -nums[i], i + 1):
                triplets.append([nums[i], nums[pair[0]], nums[pair[1]]])
        return triplets

    def twoSum(self, numbers: List[int], target: int, start: int) -> List[List[int]]:
        i, j = start, len(numbers) - 1
        pairs = []
        while i < j:
            s = numbers[i] + numbers[j]
            if s == target:
                pairs.append([i, j])
                i += 1
                j -= 1
                while i < j and numbers[i] == numbers[i - 1]:
                    i += 1
                while i < j and numbers[j] == numbers[j + 1]:
                    j -= 1
            elif s < target:
                i += 1
            else:
                j -= 1
        return pairs