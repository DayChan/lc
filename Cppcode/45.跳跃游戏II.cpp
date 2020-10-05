#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) {
        int curMaxReach = nums[0];
        int prevMaxReach = 0;
        int i = 0;
        int jumpcount = 0;
        while (prevMaxReach < nums.size()-1)
        {
            jumpcount++;
            auto nextMaxReach = curMaxReach;
            for (auto i = prevMaxReach; i <= min(curMaxReach,int(nums.size()-1)); i++)
            {
                nextMaxReach = max(nextMaxReach, i+nums[i]);
            }
            prevMaxReach = curMaxReach;
            curMaxReach = nextMaxReach;
        }
        return jumpcount;
    }
};