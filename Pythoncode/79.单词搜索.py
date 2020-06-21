class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(word, board, i, j, set()):
                    return True
        return False

    def helper(self, s, board, i, j, used):
        if len(s) == 0:
            return True
        if i < 0 or j < 0 or i > len(board) - 1 or j > len(board[0]) - 1 or (i, j) in used or board[i][j] != s[0]:
            return False
        used.add((i, j))
        if self.helper(s[1:], board, i-1, j, used):
            return True
        if self.helper(s[1:], board, i+1, j, used):
            return True
        if self.helper(s[1:], board, i, j-1, used):
            return True
        if self.helper(s[1:], board, i, j+1, used):
            return True
        used.remove((i, j))
        return False