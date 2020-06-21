class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characterset = set()
        maxsublen = 0
        j = 0
        for i in range(len(s)):
            if s[i] in characterset:
                while j < i:
                    characterset.remove(s[j])
                    if s[j] == s[i]:
                        j += 1
                        break
                    else:
                        j += 1
            characterset.add(s[i])
            maxsublen = max(maxsublen, len(characterset))
        return maxsublen