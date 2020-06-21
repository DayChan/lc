class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, -1, -1): # 从后往前找， 找到第一个可以使nums[i-1]（和nums[i:]的某个数互换）变大的i
            if i-1 >= 0 and nums[i-1] < nums[i]:
                for j in range(i, len(nums)): # 找到最小的大于nums[i-1]的数，然后和nums[i-1]互换
                    if j + 1 < len(nums) and nums[j+1] <= nums[i-1]:
                        break
                temp = nums[i-1]
                nums[i-1] = nums[j]
                nums[j] = temp
                self.reverse(nums, i, len(nums)-1) #nums[i:]一定是递减的，需要reverse一下
                return
        self.reverse(nums, 0, len(nums)-1) #如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

    def reverse(self, nums, i, j):
        while i < j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
            j -= 1
        