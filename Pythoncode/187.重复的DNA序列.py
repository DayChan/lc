class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        cache = set()
        cache2 = set()
        l = []
        for i in range(len(s) - 9):
            if s[i:i+10] in cache:
                if s[i:i+10] not in cache2:
                    cache2.add(s[i:i+10])
                    l.append(s[i:i+10])
            else:
                cache.add(s[i:i+10])
        return l


s = Solution()
s.findRepeatedDnaSequences("AAAAAAAAAAA")