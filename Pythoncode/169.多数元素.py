class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for element in nums:
            if element not in d:
                d[element] = 0
            d[element] += 1
            if d[element] > len(nums) // 2:
                return element