#include <vector>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty()) return 0;
        auto head = nums.begin();
        auto tail = head + 1;
        while (tail != nums.end())
        {
            if(*tail != *(tail-1))
            {
                *(++head) = *tail;
            }
            tail++;
        }
        return head - nums.begin() + 1;
    }
};