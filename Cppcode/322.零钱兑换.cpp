#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount+1, -1);
        dp[0] = 1;
        for (auto i = 1; i < amount+1; i++)
        {
            for (auto c: coins)
            {
                if (i-c < 0 || dp[i-c] == -1) continue;
                if (dp[i] == -1) dp[i] = dp[i-c] + 1;
                else dp[i] = min(dp[i], dp[i-c] + 1);
            }
        }
        return dp.back();
    }
};