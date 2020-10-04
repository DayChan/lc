#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        reverse(candidates.begin(), candidates.end());
        vector<vector<int>> res;
        vector<int> resEntry;
        helper(res, resEntry, candidates, target);
        return res;
    }

    void helper(vector<vector<int>>& res, vector<int> resEntry, vector<int> candidates, int target)
    {
        if (candidates.empty()) return;
        while (true)
        {
            auto s = accumulate(resEntry.begin(), resEntry.end(), 0);
            if (s < target)
            {
                helper(res, resEntry, vector<int>(candidates.begin()+1, candidates.end()), target);
            }
            else if (s == target)
            {
                res.push_back(resEntry);
            }
            else
            {
                break;
            }
            resEntry.push_back(candidates[0]);
        }
        
    }
};