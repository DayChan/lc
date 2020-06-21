class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        line_queens_count = dict() # line_queens_count[i] = the number of queens in line i
        for i in range(n):
            line_queens_count[i] = 0
        slash_queens_count = dict()
        for i in range(2*(n-1)+1):
            slash_queens_count[i] = 0
        backslash_queens_count = dict()
        for i in range(-(n-1), n):
            backslash_queens_count[i] = 0
        legal_layouts = []
        self.helper(n, 0, line_queens_count, slash_queens_count, backslash_queens_count, [], legal_layouts)
        res = []
        dot_line = ""
        for _ in range(n):
            dot_line += "."
        for legal_layout in legal_layouts:
            new_layout = []
            for _ in range(n):
                new_dot_line = dot_line[:]
                new_layout.append(new_dot_line)
            for j, i in enumerate(legal_layout):
                new_layout[i] = new_layout[i][:j] + "Q" + new_layout[i][j+1:]
            res.append(new_layout)
        return res

    def helper(self, n, queen_number, line_queens_count, slash_queens_count, backslash_queens_count, queens_layout_sofar, legal_layouts):
        if queen_number == n:
            legal_layouts.append(queens_layout_sofar)
        else:
            for i in range(n):
                if line_queens_count[i] == 0 and slash_queens_count[queen_number+i] == 0 and backslash_queens_count[queen_number-i] == 0:
                    line_queens_count[i] += 1
                    slash_queens_count[queen_number+i] += 1
                    backslash_queens_count[queen_number-i] += 1
                    new_queens_layout_sofar = queens_layout_sofar[:]
                    new_queens_layout_sofar.append(i)
                    self.helper(n, queen_number+1, line_queens_count, slash_queens_count, backslash_queens_count, new_queens_layout_sofar, legal_layouts)
                    line_queens_count[i] -= 1
                    slash_queens_count[queen_number+i] -= 1
                    backslash_queens_count[queen_number-i] -= 1

