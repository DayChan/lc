class Solution(object):
    """
    https://leetcode-cn.com/problems/trapping-rain-water/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-w-8/
    """
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_max = {}
        right_max = {}
        left_max[0] = 0
        right_max[len(height)-1] = 0
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i-1], height[i-1])
            right_max[len(height)-1-i] = max(right_max[len(height)-1-i+1], height[len(height)-1-i+1])
        water = 0
        for i in range(len(height)):
            up = min(left_max[i], right_max[i])
            if up > height[i]:
                water += up - height[i]
        return water
