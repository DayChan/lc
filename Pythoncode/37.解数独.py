class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.rowl = [set() for _ in range(9)]
        self.columnl = [set() for _ in range(9)]
        self.boxl = [[set() for _ in range(3)] for _ in range(3)]
        self.dotl = []
        for i in range(9):
            for j in range(9):
                x = board[i][j]
                if x == '.':
                    self.dotl.append((i, j))
                else:
                    self.rowl[i].add(x)
                    self.columnl[j].add(x)
                    self.boxl[i//3][j//3].add(x)
        self.helper(0, board)


    def helper(self, index, board):
        if index == len(self.dotl):
            return True
        i, j = self.dotl[index]
        for n in range(1, 10):
            number = str(n)
            if number not in self.rowl[i] and number not in self.columnl[j] and number not in self.boxl[i//3][j//3]:
                self.rowl[i].add(number)
                self.columnl[j].add(number)
                self.boxl[i//3][j//3].add(number)
                board[i][j] = number
                if self.helper(index+1, board):
                    return True
                else:
                    self.rowl[i].remove(number)
                    self.columnl[j].remove(number)
                    self.boxl[i//3][j//3].remove(number)
                    board[i][j] = '.'
        return False

