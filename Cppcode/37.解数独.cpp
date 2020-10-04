#include <vector>
#include <unordered_set>
#include <iostream>

using namespace std;

class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        vector<unordered_set<char>> rows = {unordered_set<char>(), unordered_set<char>(), unordered_set<char>(), unordered_set<char>(), unordered_set<char>(), unordered_set<char>(), unordered_set<char>(), unordered_set<char>(), unordered_set<char>()};
        vector<unordered_set<char>> cols = {unordered_set<char>(), unordered_set<char>(), unordered_set<char>(), unordered_set<char>(), unordered_set<char>(), unordered_set<char>(), unordered_set<char>(), unordered_set<char>(), unordered_set<char>()};
        vector<vector<unordered_set<char>>> boxs = {{unordered_set<char>(), unordered_set<char>(), unordered_set<char>()}, {unordered_set<char>(), unordered_set<char>(), unordered_set<char>()}, {unordered_set<char>(), unordered_set<char>(), unordered_set<char>()}};
        for (auto i = 0; i < 9; i++)
        {
            for (auto j = 0; j < 9; j++)
            {
                if (board[i][j] == '.')
                {
                    continue;
                }
                rows[i].insert(board[i][j]);
                cols[j].insert(board[i][j]);
                boxs[i/3][j/3].insert(board[i][j]);
            }
        }
        helper(board, rows, cols, boxs, 0, 0);
    }

    bool helper(vector<vector<char>>& board, vector<unordered_set<char>>& rows, vector<unordered_set<char>>& cols, vector<vector<unordered_set<char>>>& boxs, int i, int j)
    {
        if (i == board.size()) return true;
        if (board[i][j] != '.') return helper(board, rows, cols, boxs, i+(j+1)/board[0].size(), (j+1)%board[0].size());
        for (auto c : vector<char>({'1', '2', '3', '4', '5', '6', '7', '8', '9'}))
        {
            if (rows[i].count(c) == 0 && cols[j].count(c) == 0 && boxs[i/3][j/3].count(c) == 0)
            {
                board[i][j] = c;
                rows[i].insert(c);
                cols[j].insert(c);
                boxs[i/3][j/3].insert(c);
                if (helper(board, rows, cols, boxs, i+(j+1)/board[0].size(), (j+1)%board[0].size()))
                {
                    return true;
                }
                rows[i].erase(c);
                cols[j].erase(c);
                boxs[i/3][j/3].erase(c);
                board[i][j] = '.';
            }
        }
        return false;
    }
};