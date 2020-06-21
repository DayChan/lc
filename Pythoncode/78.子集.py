class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        s = []
        self.helper(nums, s, res)
        return res
    
    def helper(self, nums, s, res):
        if len(nums) == 0:
            res.append(s)
        else:
            news = s[:]
            news.append(nums[0])
            self.helper(nums[1:], news, res)
            self.helper(nums, s, res)