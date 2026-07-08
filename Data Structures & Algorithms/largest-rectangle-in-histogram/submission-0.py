class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0 
        heights = heights + [0]

        for i,h in enumerate(heights):
            while stack and heights[stack[-1]] > h :
                height = heights[stack.pop()]
                if not stack :
                    width = i 
                else :
                    width = i - 1 - stack[-1]
                max_area = max(max_area,height * width)
            stack.append(i)
        return max_area 
        