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
    void helper(string s, string p)
    {
        if (p.size() == 0 and s.size() == 0) dp[s.size()][p.size()] =  1;
        else if (p.size() == 0 and s.size() != 0) dp[s.size()][p.size()] = -1;
        else
        {
            if (p.back() != '*')
            {
                if (s.size() == 0 or (p.back() != s.back() and p.back() != '?')) dp[s.size()][p.size()] = -1;
                else dp[s.size()][p.size()] = dp[s.size()-1][p.size()-1];
            }
            else
            {
                if (dp[s.size()][p.size()-1] == 1) dp[s.size()][p.size()] =  1; // 该‘*’不匹配任何字符
                else if (s.size() > 0) dp[s.size()][p.size()] =  dp[s.size()-1][p.size()]; // 该'*'至少匹配了一个字符
                else dp[s.size()][p.size()] = -1;
            }
        }
    }
};

// int main()
// {
//     Solution s;
//     s.isMatch("aa","*");
// }