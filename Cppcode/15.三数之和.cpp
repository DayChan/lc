#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int target = 0;
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        for (auto iter = nums.begin(); iter != nums.end(); iter++)
        {
            if (iter != nums.begin() && *(iter-1) == *(iter))
            {
                continue;
            }
            auto head_ptr = iter + 1;
            auto tail_ptr = nums.end() - 1;
            while (head_ptr < tail_ptr)
            {
                if (*iter + *head_ptr + *tail_ptr < target)
                {
                    do
                    {
                        head_ptr++;
                    } while (head_ptr != nums.end() && (*head_ptr == *(head_ptr - 1)));
                }
                else if (*iter + *head_ptr + *tail_ptr == target)
                {
                    res.push_back(vector<int> ({*iter, *head_ptr, *tail_ptr}));
                    do
                    {
                        head_ptr++;
                    } while (head_ptr != nums.end() && (*head_ptr == *(head_ptr - 1)));
                    do
                    {
                        tail_ptr--;
                    } while (tail_ptr >= nums.begin() && *tail_ptr == *(tail_ptr + 1));
                }
                else
                {
                    do
                    {
                        tail_ptr--;
                    } while (tail_ptr >= nums.begin() && *tail_ptr == *(tail_ptr + 1));
                }
            }
        }
        return res;
    }
};
