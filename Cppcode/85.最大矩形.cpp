#include <vector>
#include <stack>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if (matrix.empty()) return 0;
        vector<vector<int>> matrixHeights(matrix.size(), vector<int>(matrix[0].size()));
        for (auto i = 0; i < matrix.size(); i++)
        {
            for (auto j = 0; j < matrix[0].size(); j++)
            {
                auto a = i-1>=0 ? matrixHeights[i-1][j] : 0;
                auto b = stoi(string(1, matrix[i][j]));
                if (b == 0) matrixHeights[i][j] = 0;
                else matrixHeights[i][j] = a + b;
            }
        }
        auto res = 0;
        for (auto i = 0; i < matrixHeights.size(); i++)
        {
            res = max(res, largestRectangleArea(matrixHeights[i]));
        }
        return res;
    }

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