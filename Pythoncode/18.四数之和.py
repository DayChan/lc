class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        HashMap = {}
        cache = set()

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                s = nums[i] + nums[j]
                if s not in HashMap.keys():
                    HashMap[s] = []
                HashMap[s].append([i,j])

        for s in HashMap.keys():
            if target-s not in HashMap.keys():
                pass
            else:
                for l1 in HashMap[s]:
                    for l2 in HashMap[target-s]:
                        if l1[0] not in l2 and l1[1] not in l2:
                            l = list(map(lambda index: nums[index], l1+l2))
                            # 排序后用tuple去重复
                            l.sort()
                            t = tuple(l)
                            if t not in cache:
                                cache.add(tuple(l))
                                
        return list(map(list, cache))