class Solution:
    """
    https://leetcode-cn.com/problems/3sum/solution/3sumpai-xu-shuang-zhi-zhen-yi-dong-by-jyd/
    """
    def threeSum(self, nums: [int]) -> [[int]]:
        nums.sort()
        res, k = [], 0
        for k in range(len(nums) - 2):
            if nums[k] > 0:
                break 
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            i, j = k + 1, len(nums) - 1
            while i < j: # 3. double pointer
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
        return res
