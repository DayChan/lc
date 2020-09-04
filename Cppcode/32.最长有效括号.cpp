#include <string>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

class Solution {
public:
    int longestValidParentheses(string s) {
        if (s == "") return 0;
        stack<decltype(s.size())> stk; // 里面放的都是 s 的index
        vector<int> v = vector<int> (s.size(), 0); // v[j] 记录的是以 s[j] 作为结尾的最长括号序列的长度
        for (decltype(s.size()) j = 0; j < s.size(); j++)
        {
            if (s[j] == '(')
            {
                stk.push(j);
            }
            else if (stk.size() != 0 and s[stk.top()] == '(')
            {
                auto i = stk.top();
                stk.pop();
                if (i == 0) v[j] = j - i + 1;
                else v[j] = j - i + 1 + v[i-1];
            }
            else
            {
                ;
            }
        }
        return *max_element(v.begin(), v.end());    
    }
};