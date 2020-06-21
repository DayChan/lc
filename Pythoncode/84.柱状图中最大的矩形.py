# class Solution:
#     """
#       如果heights从高到低排列或从低到高会超时
#     """
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         self.maxarea = 0
#         self.helper(heights)
#         return self.maxarea

#     def helper(self, heights):
#         if len(heights) == 0:
#             return
#         minheight = min(heights)
#         minheightindex = heights.index(minheight)
#         self.maxarea = max(minheight * len(heights), self.maxarea)
#         self.helper(heights[:minheightindex])
#         self.helper(heights[minheightindex+1:])
class Solution:
    def largestRectangleArea(self, heights) -> int:
        if len(heights) == 0:
            return 0
        d = {} # d[i] = (a, b) 第a根柱子是第i根柱子左边第一个比第i根柱子短的柱子，第b根柱子是第i根柱子右边第一个比第i根柱子短的柱子
        res = [] # res[i] = 以第i根柱子为最矮柱子所能延伸的最大面积 = heights[i] * (b - a + 1)
        stack = [] # https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/84-by-ikaruga/
        for i in range(len(heights) + 1):
            while len(stack) != 0 and (i == len(heights) or heights[stack[-1]] > heights[i]):
                l = []
                l.append(stack.pop())
                while len(stack) != 0 and heights[stack[-1]] == heights[l[-1]]: #相等的元素要一起pop出来
                    l.append(stack.pop())
                a = stack[-1] if len(stack) != 0 else -1
                b = i
                for j in l:
                    d[j] = (a, b)
            stack.append(i)
        for i in range(len(heights)):
            a, b = d[i]
            res.append(heights[i] * (b - a - 1))
        return max(res)

s = Solution()
s.largestRectangleArea([2,1,5,6,2,3])