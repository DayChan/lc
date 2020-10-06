#include <vector>
#include <stack>
#include <numeric>
#include <algorithm>

using namespace std;

class Solution {
public:
    int candy(vector<int>& ratings) {
        vector<int> canies(ratings.size(), 1);
        stack<int> stk;
        for (auto i = 0; i < ratings.size(); i++)
        {
            if (stk.empty() || ratings[stk.top()] >= ratings[i])
            {
                stk.push(i);
            }
            else
            {
                auto a = stk.top();
                stk.pop();
                canies[i] = canies[a] + 1;
                while (!stk.empty())
                {
                    auto b = stk.top();
                    stk.pop();
                    if (ratings[b] == ratings[a]) canies[b] = max(1, canies[b]); // 评分相同的，不需要糖果相同
                    else canies[b] = max(canies[a]+1, canies[b]);
                    a = b;
                }
                stk.push(i);
            }
        }
        auto a = stk.top();
        stk.pop();
        while (!stk.empty())
        {
            auto b = stk.top();
            stk.pop();
            if (ratings[b] == ratings[a]) canies[b] = max(1, canies[b]); // 评分相同的，不需要糖果相同
            else canies[b] = max(canies[a]+1, canies[b]);
            a = b;
        }
        return accumulate(canies.begin(), canies.end(), 0);
    }
};