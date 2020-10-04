#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        unordered_set<string> visited;
        for (auto i = 0; i < board.size(); i++)
        {
            for (auto j = 0; j < board[0].size(); j++)
            {
                if (board[i][j] == word[0])
                {
                    visited.insert(to_string(i)+" "+to_string(j));
                    if (helper(board, visited, string(word.begin()+1, word.end()), i, j)) return true;
                    visited.erase(to_string(i)+" "+to_string(j));
                }
            }
        }
        return false;
    }

    bool helper(vector<vector<char>>& board, unordered_set<string>& visited, string word, int i, int j)
    {
        if (word.size() == 0) return true;
        if (i-1>=0 && board[i-1][j] == word[0] &&  visited.count(to_string(i-1)+" "+to_string(j)) == 0)
        {
            visited.insert(to_string(i-1)+" "+to_string(j));
            if (helper(board, visited, string(word.begin()+1, word.end()), i-1, j)) return true;
            visited.erase(to_string(i-1)+" "+to_string(j));
        }
        if (i+1<board.size() && board[i+1][j] == word[0] &&  visited.count(to_string(i+1)+" "+to_string(j)) == 0)
        {
            visited.insert(to_string(i+1)+" "+to_string(j));
            if (helper(board, visited, string(word.begin()+1, word.end()), i+1, j)) return true;
            visited.erase(to_string(i+1)+" "+to_string(j));
        }
        if (j-1>=0 && board[i][j-1] == word[0] &&  visited.count(to_string(i)+" "+to_string(j-1)) == 0)
        {
            visited.insert(to_string(i)+" "+to_string(j-1));
            if (helper(board, visited, string(word.begin()+1, word.end()), i, j-1)) return true;
            visited.erase(to_string(i)+" "+to_string(j-1));
        }
        if (j+1<board[0].size() && board[i][j+1] == word[0] &&  visited.count(to_string(i)+" "+to_string(j+1)) == 0)
        {
            visited.insert(to_string(i)+" "+to_string(j+1));
            if (helper(board, visited, string(word.begin()+1, word.end()), i, j+1)) return true;
            visited.erase(to_string(i)+" "+to_string(j+1));
        }
        return false;
    }
};