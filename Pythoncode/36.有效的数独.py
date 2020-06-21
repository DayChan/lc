class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowl = [set() for _ in range(9)]
        columnl = [set() for _ in range(9)]
        boxl = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                x = board[i][j]
                if x == '.':
                    pass
                elif x in rowl[i] or x in columnl[j] or x in boxl[i//3][j//3]:
                    return False
                else:
                    rowl[i].add(x)
                    columnl[j].add(x)
                    boxl[i//3][j//3].add(x)
        return True
        