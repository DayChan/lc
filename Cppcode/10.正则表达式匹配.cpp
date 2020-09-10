#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> dp;

    bool isMatch(string s, string p) {
        dp = vector<vector<int>> (s.size()+1, vector<int>(p.size()+1, 0));
        for (decltype(s.size()) i = 0; i <= s.size(); i++)
        {
            for (decltype(p.size()) j = 0; j <= p.size(); j++)
            {
                helper(s.substr(0, i), p.substr(0, j));
            }
        }
        if (dp[s.size()][p.size()] == 1) return true;
        else return false;
    }    

    void helper(string s, string p) {
        if (s.size() == 0 && p.size() == 0) dp[s.size()][p.size()] = 1;
        else if (s.size() != 0 && p.size() == 0) dp[s.size()][p.size()] = -1;
        else
        {
            if (p.back() != '*')
            {
                if (s.size() == 0 || (s.back() != p.back() && p.back() != '.')) dp[s.size()][p.size()] = -1;
                else dp[s.size()][p.size()] = dp[s.size()-1][p.size()-1];
            }
            else
            {
                if (dp[s.size()][p.size()-2] == 1) dp[s.size()][p.size()] = 1; // '*' 匹配了0个
                else if (s.size() > 0 && (p[p.size()-2] == '.' || p[p.size()-2] == s.back())) dp[s.size()][p.size()] = dp[s.size()-1][p.size()]; // '*' 匹配了至少1个
                else dp[s.size()][p.size()] = -1;
            }
        }
    }
};