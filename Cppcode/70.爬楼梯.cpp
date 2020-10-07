#include <vector>

using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        vector<int> dp(n+1);
        for (auto i = 0; i < n+1; i++)
        {
            if (i == 0)
            {
                dp[i] = 1;
                continue;
            }
            auto a = i-2>=0 ? dp[i-2] : 0;
            auto b = i-1>=0 ? dp[i-1] : 0;
            dp[i] = a + b;
        }
        return dp[n];
    }
};