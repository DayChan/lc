#include <vector>
#include <string>


using namespace std;

class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> res;
        helper(s, 4, "", res);
        return res;
    }
    void helper(string s, int un_fill_space, string cur_ip, vector<string>& res)
    {
        if (un_fill_space == 0 && s.empty())
        {
            res.push_back(cur_ip.substr(1));
        }
        else if (s.empty() || un_fill_space == 0)
        {
            return;
        }
        else if (s[0] == '0')
        {
            helper(s.substr(1), un_fill_space-1, cur_ip+"."+"0", res);
        }
        else
        {
            for (size_t si = 1; si <= 3 && si <= s.size(); si++)
            {
                if (stoi(s.substr(0, si))>255) break;
                helper(s.substr(si), un_fill_space-1, cur_ip+"."+s.substr(0, si), res);
            }
        }
    }
};