#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target)
    {
        unordered_map<int, int> m;
        vector<int> res;
        for (auto iter = nums.begin(); iter != nums.end(); iter++)
        {
            if (m.find(*iter) != m.end())
            {
                res.push_back(iter - nums.begin());
                res.push_back(m[*iter]);
                break;
            }
            else
            {
                m[target - *iter] = iter - nums.begin();
            }
        }
        return res;
    }
};