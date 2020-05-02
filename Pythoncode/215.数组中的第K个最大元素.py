from queue import PriorityQueue
class Solution:
    def findKthLargest(self, nums, k):
        pq = PriorityQueue()
        pq_size = 0
        for i in range(len(nums)):
            if pq_size < k:
                pq_size += 1
                pq.put((nums[i], i))
            else:
                pq.put((nums[i], i))
                pq.get()
        return pq.get()[0]

# s = Solution()
# print(s.findKthLargest([3,2,1,5,6,4], 2))