#include <vector>

using namespace std;

class Solution {
public:
    int numTrees(int n) {
        vector<int> dp;
        dp.push_back(1);
        for (auto i = 1; i <= n; i++)
        {
            auto a = 0;
            for (auto j = 0; j < i; j++)
            {
                a += dp[j] * dp[i-j-1];
            }
            dp.push_back(a);
        }
        return dp.back();
    }
};