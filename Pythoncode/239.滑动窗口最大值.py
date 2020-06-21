class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        https://leetcode-cn.com/problems/sliding-window-maximum/solution/dan-diao-dui-lie-by-labuladong/
        """
        monotonous_queue = []
        res = []
        for i in range(len(nums)):
            while len(monotonous_queue) != 0 and nums[monotonous_queue[-1]] <= nums[i]:
                monotonous_queue.pop(-1)
            monotonous_queue.append(i)
            if i >= k - 1:
                if monotonous_queue[0] == i - k:
                    monotonous_queue.pop(0)
                res.append(nums[monotonous_queue[0]])
        return res

