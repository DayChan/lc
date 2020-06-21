class Solution:
    def searchRange(self, nums, target: int):
        guard = self.bin_search(nums, target, 0, len(nums)-1)
        if guard == -1:
            return [-1, -1]
        return [self.my_bin_search_left(nums, target, 0, guard), self.my_bin_search_right(nums, target, guard, len(nums)-1)]
    def bin_search(self, nums, target, head, tail):
        if head > tail:
            return -1
        else:
            mid = (head + tail) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                head = mid + 1
            else:
                tail = mid - 1
            return self.bin_search(nums, target, head, tail)


    def my_bin_search_left(self, nums, target, head, tail):
        if head == tail:
            return head
        else:
            mid = (head + tail) // 2    
            if nums[mid] == target:
                tail = mid
            else:
                head = mid + 1
            return self.my_bin_search_left(nums, target, head, tail)



    def my_bin_search_right(self, nums, target, head, tail):
        if head == tail:
            return head
        else:
            mid = (head + tail + 1) // 2    
            if nums[mid] == target:
                # if mid == head:
                #     if nums[tail] == target:
                #         return tail
                #     else:
                #         return head
                head = mid
            else:
                tail = mid - 1
            return self.my_bin_search_right(nums, target, head, tail)