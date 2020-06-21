class Solution:
    def groupAnagrams(self, strs):
        hashMap = {}
        for string in strs:
            self.helper(hashMap, string)
        return list(hashMap.values())

    def helper(self, hm, string):
        l = list(string)
        l.sort()
        hashcode = tuple(l)
        if hashcode not in hm.keys():
            hm[hashcode] = []
        hm[hashcode].append(string)

s = Solution()
s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])