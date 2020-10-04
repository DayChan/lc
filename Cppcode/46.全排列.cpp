#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> cur;
        helper(cur, nums, res);
        return res;
    }
    void helper(vector<int> cur, vector<int> nums, vector<vector<int>>& res)
    {
        if (nums.empty())
        {
            res.push_back(cur);
        }
        for(auto iter = nums.begin(); iter != nums.end(); iter++)
        {
            vector<int> new_cur = cur;
            new_cur.push_back(*iter);
            vector<int> new_nums;
            new_nums.insert(new_nums.end(), nums.begin(), iter);
            new_nums.insert(new_nums.end(), iter+1, nums.end());
            helper(new_cur, new_nums, res);
        }
    }
};