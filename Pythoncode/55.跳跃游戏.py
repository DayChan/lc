class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        https://www.cnblogs.com/grandyang/p/4371526.html
        '''
        reach = 0 + nums[0]
        for i in range(len(nums)):
            if i > reach:
                return False
            else:
                reach = max(reach, i + nums[i])
        return True