#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        vector<vector<int>> dp(text1.size(), vector<int>(text2.size(), 0));
        for (auto i = 0; i < text1.size(); i++)
        {
            for (auto j = 0; j < text2.size(); j++)
            {
                auto a = i-1>=0 ? dp[i-1][j] : 0;
                auto b = j-1>=0 ? dp[i][j-1] : 0;
                auto c = text1[i] == text2[j] ? 1 : 0;
                if (i-1>=0 && j-1>=0) c += dp[i-1][j-1];
                dp[i][j] = max(max(a, b) ,c);
            }
        }
        return dp.back().back();
    }
};