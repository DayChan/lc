class Solution:
    """
    https://leetcode-cn.com/problems/remove-invalid-parentheses/solution/pythontong-su-yi-dong-de-bfsjie-fa-by-mai-mai-mai-/
    """
    def removeInvalidParentheses(self, s):
        def isvalid(s):  # 判断括号串是否合法
            stack = []
            for i in range(len(s)):
                if s[i] == "(":
                    stack.append(i)
                elif s[i] == ")":
                    if len(stack) != 0 and s[stack[-1]] == "(":
                        stack.pop()
                    else:
                        stack.append(i)
            return len(stack) == 0

        level = {s}
        while True:  # BFS
            valid = list(filter(isvalid, level))
            if len(valid) != 0:
                return valid
            level = {s[:i] + s[i + 1:] for s in level for i in range(len(s)) if s[i] in '()'}
        