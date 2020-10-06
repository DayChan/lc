#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        vector<int> res(T.size(), 0);
        stack<int> stk;
        for (auto i = 0; i < T.size(); i++)
        {
            if (stk.empty() || T[stk.top()] >= T[i])
            {
                stk.push(i);
            }
            else
            {
                while (!stk.empty() && T[stk.top()] < T[i])
                {
                    auto a = stk.top();
                    stk.pop();
                    res[a] = i - a;
                }
                stk.push(i);
            }
        }
        while (!stk.empty())
        {
            auto a = stk.top();
            stk.pop();
            res[a] = 0;
        }
        return res;
    }
};