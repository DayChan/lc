class Solution:
    """
    https://leetcode-cn.com/problems/longest-consecutive-sequence/solution/128ha-xi-biao-by-genjie-li/
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        maxsublen = 1
        numset = set(nums)
        for x in numset:
            if x-1 in numset:
                pass
            else:
                counter = 1
                while x + counter in numset:
                    counter += 1
                maxsublen = max(maxsublen, counter)
        return maxsublen