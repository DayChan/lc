#include <vector>

using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        return helper(nums, target, 0, nums.size()-1);
    }

    int helper(vector<int>& nums, int target, int head, int tail)
    {
        if (tail < head) {
            return -1;
        }
        auto mid = (head + tail) / 2;
        if (nums[head] <= nums[tail])
        {
            if (target == nums[mid])
            {
                return mid;
            }
            else if (target < nums[mid])
            {
                return helper(nums, target, head, mid-1);
            }
            else
            {
                return helper(nums, target, mid+1, tail);
            }
        }
        else
        {
            if (target == nums[mid])
            {
                return mid;
            }
            if (nums[mid] <= nums[tail])
            {
                if (target < nums[mid])
                {
                    return helper(nums, target, head, mid-1);
                }
                else if (target > nums[mid] && target <= nums[tail]) {
                    return helper(nums, target, mid+1, tail);
                }
                else
                {
                    return helper(nums, target, head, mid-1);
                }
            }
            else // nums[mid] >= nums[head]
            {
                if (target > nums[mid])
                {
                    return helper(nums, target, mid+1, tail);
                }
                else if (target < nums[mid] && target >= nums[head])
                {
                    return helper(nums, target, head, mid-1);
                }
                else
                {
                    return helper(nums, target, mid+1, tail);
                }
            }
        }
    }
};
