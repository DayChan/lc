#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minDistance(string word1, string word2) {
        vector<vector<int>> dp(word1.size()+1, vector<int>(word2.size()+1, 0));
        for (size_t i = 0; i <= word1.size(); i++)
        {
            for (size_t j = 0; j <= word2.size(); j++)
            {
                helper(i, j, word1, word2, dp);
            }
        }
        return dp[word1.size()][word2.size()];
    }
    void helper(const size_t i, const size_t j, const string& word1, const string& word2, vector<vector<int>>& dp)
    {
        if (i == 0 or j == 0)
        {
            dp[i][j] = i+j;
        }
        else if (word1[i-1] == word2[j-1])
        {
            dp[i][j] = dp[i-1][j-1];
        }
        else
        {
            auto a = dp[i][j-1] + 1; //增
            auto b = dp[i-1][j] + 1; //删
            auto c = dp[i-1][j-1] + 1; //改
            dp[i][j] = min({a, b, c});
        }
    }
};