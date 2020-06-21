class Solution:
    """
    https://leetcode-cn.com/problems/minimum-window-substring/solution/hua-dong-chuang-kou-suan-fa-tong-yong-si-xiang-by-/
    """
    def minWindow(self, s: str, t: str) -> str:
        needs = {}
        window = {}
        for c in t:
            if c not in needs:
                needs[c] = 0
                window[c] = 0
            needs[c] += 1
        satified = 0 # how many characters have been satified, if satified == len(needs) all characters have been satified
        i = 0
        j = 0
        minlen = float("inf")
        res = ""
        while j < len(s):
            if s[j] not in needs:
                pass
            else:
                window[s[j]] += 1
                if window[s[j]] == needs[s[j]]:
                    satified += 1
                    if satified == len(needs):
                        while satified == len(needs): #after this while s[i-1:j+1] can satify, s[i:j+1] can not
                            if s[i] not in needs:
                                pass
                            else:
                                window[s[i]] -= 1
                                if window[s[i]] < needs[s[i]]:
                                    satified -= 1
                                else:
                                    pass
                            i += 1
                        if j - (i - 1) + 1 < minlen:
                            minlen = j - (i - 1) + 1
                            res = s[i-1:j+1]
                    else:
                        pass
                else:
                    pass
            j += 1
        return res