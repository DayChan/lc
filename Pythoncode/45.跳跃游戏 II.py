class Solution:
    def jump(self, nums: List[int]) -> int:
        # '''
        # https://blog.csdn.net/fuxuemingzhu/article/details/84578893
        # '''
        # pos = 0
        # cur = 0
        # pre = 0
        # counter = 0
        # while cur < len(nums)-1:
        #     counter += 1
        #     pre = cur
        #     for i in range(pos, pre+1):
        #         if cur < i + nums[i]:
        #             cur = i + nums[i]
        #             pos = i
        # return counter
        counter = 0
        jumppoint = 0
        maxlandingpoint = jumppoint
        while maxlandingpoint < len(nums) - 1:
            nextjumppoint = jumppoint
            nextmaxlandingpoint = maxlandingpoint
            for i in range(jumppoint, maxlandingpoint+1):
                if i + nums[i] > nextmaxlandingpoint:
                    nextjumppoint = i
                    nextmaxlandingpoint = i + nums[i]
            jumppoint = nextjumppoint
            maxlandingpoint = nextmaxlandingpoint
            counter += 1
        return counter

