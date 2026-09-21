class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        biggest_a = 0
        for i in range(len(heights)):
            while stack and stack[-1][0] > heights[i]:
                height, start = stack.pop()
                width = i if not stack else i - stack[-1][1] - 1
                biggest_a = max(biggest_a, height * width)
            stack.append((heights[i], i))

        n = len(heights)
        while stack:
            height, start = stack.pop()
            width = n if not stack else n - stack[-1][1] - 1
            biggest_a = max(biggest_a, height * width)

        return biggest_a