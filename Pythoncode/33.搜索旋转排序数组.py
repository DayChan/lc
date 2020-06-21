class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        start = 0
        end = len(nums) - 1

        if target >= nums[0]: # target on the left
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] < nums[start] or target < nums[mid]:
                    end = mid - 1
                elif target > nums[mid]:
                    start = mid + 1
                else:
                    return mid

        else: #target on the right
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] > nums[end] or target > nums[mid]:
                    start = mid + 1
                elif target < nums[mid] :
                    end = mid - 1 
                else:
                    return mid
        
        return -1



