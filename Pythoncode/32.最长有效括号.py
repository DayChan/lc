class Solution:
    """
    https://leetcode-cn.com/problems/longest-valid-parentheses/solution/zui-chang-you-xiao-gua-hao-by-powcai/
    """
    def longestValidParentheses(self, s: str) -> int:
        if  len(s) == 0:
            return 0
        res = []
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if len(stack) != 0 and s[stack[-1]] == "(":
                    res.append(stack.pop())
                    res.append(i)
                else:
                    stack.append(i)
        res.sort()
        i = 0
        maxlen = 0
        while i < len(res):
            j = i
            while j < len(res) and res[j] - res[i] == j - i:
                maxlen = max(maxlen, j - i + 1)
                j += 1
            i = j
        return maxlen
