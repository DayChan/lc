#include <vector>
#include <stack>
using namespace std;

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int maxExtendSize = 0;
        stack<int> stk;
        for (int i = 0; i < heights.size(); i++)
        {
            if (stk.empty() || heights[stk.top()] <= heights[i])
            {
                stk.push(i);
            }
            else
            {
                while (!stk.empty() && heights[stk.top()] > heights[i])
                {
                    int a = stk.top();
                    stk.pop();
                    while (!stk.empty() && heights[stk.top()] == heights[a])
                    {
                        a = stk.top();
                        stk.pop();
                    }
                    int rightStop = i;
                    int leftStop = stk.empty()?-1:stk.top();
                    int extendSize = (rightStop - leftStop - 1) * heights[a];
                    maxExtendSize = max(maxExtendSize, extendSize);
                }
                stk.push(i);
            }
        }
        int i = heights.size();
        while (!stk.empty())
        {
            int a = stk.top();
            stk.pop();
            while (!stk.empty() && heights[stk.top()] == heights[a])
            {
                a = stk.top();
                stk.pop();
            }
            int rightStop = i;
            int leftStop = stk.empty()?-1:stk.top();
            int extendSize = (rightStop - leftStop - 1) * heights[a];
            maxExtendSize = max(maxExtendSize, extendSize);
        }
        return maxExtendSize;
    }
};