class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        while j + 1 < len(nums):
            if nums[j+1] != nums[j]:
                i += 1
                nums[i] = nums[j+1]
            j += 1
        return i + 1