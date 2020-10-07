#include <climits>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        vector<vector<int>> pathSum(grid.size(), vector<int>(grid[0].size()));
        for (auto i = 0; i < grid.size(); i++)
        {
            for (auto j = 0; j < grid[0].size(); j++)
            {
                if (i == 0 && j == 0)
                {
                    pathSum[i][j] = grid[i][j];
                    continue;
                }
                auto a = i-1>=0 ? pathSum[i-1][j] : INT_MAX;
                auto b = j-1>=0 ? pathSum[i][j-1] : INT_MAX;
                pathSum[i][j] = min(a, b) + grid[i][j];
            }
        }
        return pathSum[grid.size()-1][grid[0].size()-1];
    }
};