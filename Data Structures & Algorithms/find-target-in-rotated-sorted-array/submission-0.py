class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lower, upper = 0, n - 1
        while lower < upper:
            mid = lower + (upper - lower) // 2
            if nums[mid] > nums[upper]:
                lower = mid + 1
            else:
                upper = mid
        pivot = lower

        lower, upper = 0, n - 1
        while lower <= upper:
            offset = lower + (upper - lower) // 2
            actual = (pivot + offset) % n
            if nums[actual] == target:
                return actual
            elif nums[actual] < target:
                lower = offset + 1
            else:
                upper = offset - 1
        return -1