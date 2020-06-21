class Solution:
    """
    https://leetcode-cn.com/problems/maximum-subarray/solution/zui-da-zi-xu-he-cshi-xian-si-chong-jie-fa-bao-li-f/
    """
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]] # dp[i] = 以nums[i]结尾的最大自序和
        for i in range(1, len(nums)):
            dp.append(max(nums[i], nums[i] + dp[i-1]))
        return max(dp)
