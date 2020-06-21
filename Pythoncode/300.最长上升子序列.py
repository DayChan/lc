class Solution:
    def lengthOfLIS(self, nums):
        if len(nums) == 0:
            return 0
        dp = {} # dp[i] = 以nums[i]作结尾的最长上升子序列的长度
        for i in range(len(nums)):
            if i == 0:
                dp[0] = 1
            else:
                dp[i] = max(dp[j] if nums[j] < nums[i] else 0 for j in range(i)) + 1
        return max(dp.values())

s = Solution()
s.lengthOfLIS([10,9,2,5,3,7,101,18])