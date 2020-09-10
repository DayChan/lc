#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> wordSet;
        for (auto s: wordDict) wordSet.insert(s);
        vector<bool> dp(s.size(), false);
        for (auto j = 0; j < dp.size(); j++)
        {
            for (auto i = -1; i < j; i++)
            {
                if (i >= 0 && !dp[i]) continue;
                if (wordSet.count(s.substr(i+1, j-i)) != 0)
                {
                    dp[j] = true;
                    break;
                }
            }
        }
        return dp.back();
    }
};