class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.helper(candidates, target, 0, [], res)
        return res
    def helper(self, candidates, target, sum_so_far, candidates_so_far, res):
        if sum_so_far == target:
            res.append(candidates_so_far)
        for i in range(len(candidates)):
            n = candidates[i]
            if sum_so_far + n > target:
                break
            else:
                new_candidates_so_far = candidates_so_far[:]
                new_candidates_so_far.append(n)
                self.helper(candidates[i:], target, sum_so_far+n, new_candidates_so_far, res)