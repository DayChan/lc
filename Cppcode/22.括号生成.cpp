#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        if (n == 0) return res;
        helper(n, n, res, "");
        return res;
    }

    void helper(int left_bracket_num, int right_bracket_num, vector<string> &res, string cur_string)
    {
        if (left_bracket_num == 0 and right_bracket_num == 0) res.push_back(cur_string);
        if (left_bracket_num > 0) helper(left_bracket_num-1, right_bracket_num, res, cur_string+'(');
        if (right_bracket_num > 0 and right_bracket_num - 1 >= left_bracket_num) helper(left_bracket_num, right_bracket_num-1, res, cur_string+")");
    }
};