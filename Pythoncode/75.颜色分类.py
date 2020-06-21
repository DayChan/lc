class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        head = 0
        tail = len(nums) - 1
        left_most_one = None
        while head <= tail:
            if nums[head] == 0:
                if left_most_one != None: #如果这个0前面有1，就把这个0和最前面的1交换
                    nums[left_most_one], nums[head] = nums[head], nums[left_most_one]
                    left_most_one += 1
                head += 1
            elif nums[head] == 2: #2一定得在后面，所以把这个2和后面的tail换，然后下一个循环再检查换过来的是什么东西
                nums[head], nums[tail] = nums[tail], nums[head]
                tail -= 1
            else:
                if left_most_one == None:
                    left_most_one = head
                head += 1
        return nums
