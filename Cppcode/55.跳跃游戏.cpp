#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int maxReachPoint = 0;
        int i = 0;
        while (i <= maxReachPoint)
        {
            if (i == nums.size()-1) return true;
            maxReachPoint = max(maxReachPoint, i+nums[i]);
            i++;
        }
        return false;
    }
};