class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if len(stack) == 0:
                stack.append(x)
            elif stack[-1] == "(" and x == ")":
                stack.pop()
            elif stack[-1] == "{" and x == "}":
                stack.pop()
            elif stack[-1] == "[" and x == "]":
                stack.pop()
            else:
                stack.append(x)
        return len(stack) == 0
        
s = Solution()
s.isValid("()")