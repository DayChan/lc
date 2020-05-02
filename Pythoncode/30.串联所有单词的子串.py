class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0 or len(s) == 0:
            return []
        word2num = {}
        wordlength = len(words[0])
        wordslength = wordlength * len(words)
        l = []
        for word in words:
            if word not in word2num.keys():
                word2num[word] = 1
            else:
                word2num[word] += 1
        for i in range(len(s)-wordslength+1):
            cache = word2num.copy()
            for head in range(i, i+wordslength, wordlength):
                w = s[head:head+wordlength]
                if w not in cache.keys():
                    break
                elif cache[w] == 0:
                    break
                else:
                    cache[w] -= 1
                if head == i + wordslength - wordlength:
                    l.append(i)
        return l

s = Solution()
s.findSubstring("barfoothefoobarman", ["foo","bar"])