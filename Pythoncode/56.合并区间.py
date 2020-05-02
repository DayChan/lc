class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda l: l[0]) # sort by start
        merged = []
        for l in intervals:
            if len(merged) == 0 or l[0] > merged[-1][1]: # no over lap
                merged.append(l)
            else: # over lap
                merged[-1][1] = max(merged[-1][1], l[1])
        return merged