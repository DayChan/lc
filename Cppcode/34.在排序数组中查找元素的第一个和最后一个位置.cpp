#include <vector>

using namespace std;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        auto a = binanrySearch(nums, target, 0, nums.size()-1);
        if (a == -1)
        {
            return vector<int> {-1, -1};
        }
        else
        {
            return vector<int> {binanrySearchLeft(nums, target, 0, a), binanrySearchRight(nums, target, a, nums.size()-1)};
        }
    }

    int binanrySearch(vector<int>& nums, int target, int head, int tail)
    {
        if (tail < head) {
            return -1;
        }
        auto mid = (head + tail) / 2;
        if (target == nums[mid])
        {
            return mid;
        }
        else if (target < nums[mid])
        {
            return binanrySearch(nums, target, head, mid-1);
        }
        else
        {
            return binanrySearch(nums, target, mid+1, tail);
        }
    }

    int binanrySearchLeft(vector<int>& nums, int target, int head, int tail)
    {
        auto mid = (head + tail) / 2;
        if (target == nums[mid] && (mid-1 == -1 || nums[mid-1] != target))
        {
            return mid;
        }
        else if (target == nums[mid])
        {
            return binanrySearchLeft(nums, target, head, mid-1);
        }
        else
        {
            return binanrySearchLeft(nums, target, mid+1, tail);
        }
    }

    int binanrySearchRight(vector<int>& nums, int target, int head, int tail)
    {
        auto mid = (head + tail) / 2;
        if (target == nums[mid] && (mid+1 == nums.size() || nums[mid+1] != target))
        {
            return mid;
        }
        else if (target == nums[mid])
        {
            return binanrySearchRight(nums, target, mid+1, tail);
        }
        else
        {
            return binanrySearchRight(nums, target, head, mid-1);
        }
    }
};