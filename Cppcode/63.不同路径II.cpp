#include <vector>

using namespace std;

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        auto m = obstacleGrid.size();
        auto n = obstacleGrid[0].size();
        vector<vector<int>> dp(m, vector<int>(n));
        for (auto i = 0; i < m; i++)
        {
            for (auto j = 0; j < n; j++)
            {
                if (obstacleGrid[i][j] == 1)
                {
                    dp[i][j] = 0;
                    continue;
                }
                if (i == 0 && j == 0)
                {
                    dp[i][j] = 1;
                    continue;
                }
                auto a = i-1>=0 ? dp[i-1][j] : 0;
                auto b = j-1>=0 ? dp[i][j-1] : 0;
                dp[i][j] = a + b;
            }
        }
        return dp[m-1][n-1];
    }
};