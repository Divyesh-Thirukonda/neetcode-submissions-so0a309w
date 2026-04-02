class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0) # for truncation
        stack = []
        res = 0

        for i in range(len(heights)):
            if (not stack) or (heights[i] >= stack[-1][1]):
                stack.append((i, heights[i]))
            else:
                newI = i
                while stack and heights[i] < stack[-1][1]:
                    idx, val = stack.pop()

                    curr = (i - idx) * val # or heights[i]?
                    newI = idx
                    res = max(res, curr)
                stack.append((newI, heights[i]))

        return res