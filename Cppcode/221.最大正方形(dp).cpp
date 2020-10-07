#include <vector>
#include <algorithm>

using namespace std;

class Solution {
    // https://leetcode-cn.com/problems/maximal-square/solution/li-jie-san-zhe-qu-zui-xiao-1-by-lzhlyle/
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        if (matrix.empty()) return 0;
        vector<vector<int>> dp(matrix.size(), vector<int>(matrix[0].size())); // dp[i][j] 以i,j为右下角元素的最大正方形的边长
        auto res = 0;
        for (auto i = 0; i < matrix.size(); i++)
        {
            for (auto j = 0; j < matrix.size(); j++)
            {
                if (matrix[i][j] == '0')
                {
                    dp[i][j] = 0;
                    continue;
                }
                auto a = i-1>=0&&j-1>=0 ? dp[i-1][j-1] : 0;
                auto b = i-1>=0 ? dp[i-1][j] : 0;
                auto c = j-1>=0 ? dp[i][j-1] : 0;
                dp[i][j] = min(min(a, b), c) + 1;
                res = max(res, dp[i][j]);
            }
        }
        return res*res;
    }
};