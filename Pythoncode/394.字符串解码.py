class Solution:
    def decodeString(self, s: str) -> str:
        num_set = set(["0","1","2","3","4","5","6","7","8","9"])
        res = ""
        i = 0
        while i < len(s):
            if s[i] not in num_set: #是字母
                res += s[i]
            else: #nums[i]是数字
                j = i+1
                while s[j] in num_set:
                    j += 1
                num = int(s[i:j])
                i = j - 1 #nums[i]是数字，所以nums[i+1]是“[”
                i, sinbrackets = self.helper(s, i+2) #返回值nums[i]是“]”, sinbrackets 是[]内的string
                res += num*sinbrackets
            i += 1
        return res

    def helper(self, s, i):
        num_set = set(["0","1","2","3","4","5","6","7","8","9"])
        res = ""
        while s[i] != "]":
            if s[i] not in num_set: #是字母
                res += s[i]
            else: #nums[i]是数字
                j = i+1
                while s[j] in num_set:
                    j += 1
                num = int(s[i:j])
                i = j - 1 #nums[i]是数字，所以nums[i+1]是“[”
                i, sinbrackets = self.helper(s, i+2)
                res += num*sinbrackets
            i += 1
        return i, res
            
s = Solution()
s.decodeString("3[a]2[bc]")