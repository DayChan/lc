#include <vector>
#include <algorithm>

using namespace std;

class Solution {
    //https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/dong-tai-gui-hua-er-fen-cha-zhao-tan-xin-suan-fa-p/
public:
    int lengthOfLIS(vector<int>& nums) {
        if (nums.empty()) return 0;
        vector<int> dp;
        for (auto i = 0; i < nums.size(); i++)
        {
            auto maxlength = 1;
            for (auto j = 0; j < i; j++)
            {
                if (nums[j] < nums[i])
                {
                    maxlength = max(maxlength, dp[j]+1);
                }   
            }
            dp.push_back(maxlength);
        }
        return *max_element(dp.begin(), dp.end());
    }
};