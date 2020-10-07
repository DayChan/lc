#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        vector<int> dp; // dp[i] = 以nums[i]作为结尾的最大子序和
        for (auto i = 0; i < nums.size(); i++)
        {
            if (i == 0 || dp[i-1] <= 0)
            {
                dp.push_back(nums[i]);
            }
            else
            {
                dp.push_back(nums[i]+dp[i-1]);
            }
        }
        return *max_element(dp.begin(), dp.end());
    }
};