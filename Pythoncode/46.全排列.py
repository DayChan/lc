class Solution:
    def permute(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        returnl = []
        for i in range(len(nums)):
            returnl.extend([l + [nums[i]] for l in self.permute(nums[:i]+nums[i+1:])])
        return returnl

# s = Solution()
# print(s.permute([1,2,3]))
