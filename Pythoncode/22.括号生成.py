class Solution:
    """
    https://leetcode-cn.com/problems/generate-parentheses/solution/hui-su-suan-fa-by-liweiwei1419/
    """
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        leftnum = n
        rightnum = n
        self.helper(leftnum, rightnum, "", res)
        return res
    
    def helper(self, leftnum, rightnum, s, res):
        if leftnum == 0 and rightnum == 0:
            res.append(s)
        if leftnum != 0:
            copys = s[:]
            copys += "("
            self.helper(leftnum-1, rightnum, copys, res)
        if rightnum - 1 >= leftnum:
            copys = s[:]
            copys += ")"
            self.helper(leftnum, rightnum-1, copys, res)