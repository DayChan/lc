class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = 0
        j = 0
        if len(s) == 0 and len(p) == 0:
            return True
        if len(p) == 0 and len(s) != 0:
            return False
            
        if len(p) == 1 or p[j+1] != "*": # 第 j+1 位不是 * ，所以 p[j] 和 s[j] 一定要匹配上
            if len(s) == 0 or (p[j] != "." and p[j] != s[i]): # p[j] 和 s[j] 没匹配上
                return False
            return self.isMatch(s[i+1:], p[j+1:]) # p[j] 和 s[j] 匹配上了
        else: # 第 j+1 是 *，所以 p[j] 可以不匹配 s 里的字母，或匹配 s[i], 或 s[i], s[i+1], 或 s[i], s[i+1]，s[i+2].......
            if self.isMatch(s[i:], p[j+2:]):
                return True
            while i < len(s) and (p[j] == "." or s[i] == p[j]):
                if self.isMatch(s[i+1:], p[j+2:]):
                    return True
                i += 1
            return False