#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        int water_size = 0;
        stack<decltype(height.begin())> stk;
        for (auto iter = height.begin(); iter != height.end(); iter++)
        {
            if (stk.empty() || *(stk.top()) >= *iter)
            {
                stk.push(iter);
            }
            else
            {
                while (stk.size() >= 2 && *(stk.top()) < *iter)
                {
                    auto b = stk.top();
                    stk.pop();
                    auto a = stk.top();
                    auto c = iter;
                    water_size += (c - a -1) * (min(*a, *c) - *b);
                }
                if (*(stk.top()) < *iter) stk.pop();
                stk.push(iter);
            }
        }
        return water_size;
    }
};