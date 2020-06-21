class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        cache = set()
        res = ""
        words.sort(key=lambda s: -(len(s))) #先看长的单词，再看短的单词
        for s in words:
            if s not in cache:
                res += s
                res += "#"
                for i in range(len(s)):
                    cache.add(s[i:])
        return len(res)