#include <vector>
#include <string>
#include <unordered_set>
#include <climits>

using namespace std;

class Solution {
public:
    int min_del_times = INT_MAX;

    vector<string> removeInvalidParentheses(string s) {
        unordered_set<string> res;
        int right_undecided_right_bracket_num = 0;
        for (char c : s)
        {
            if (c == ')') right_undecided_right_bracket_num++;
        }
        helper(0, 0, right_undecided_right_bracket_num, res, s, 0, "");
        return vector<string> (res.begin(), res.end());
    }
    void helper(int del_times, int left_unmatch_left_bracket_count, int right_undecided_right_bracket_num, unordered_set<string> &res, const string &s, size_t index, string cur_string)
    {
        if (del_times > min_del_times) return;
        if (left_unmatch_left_bracket_count < 0 or left_unmatch_left_bracket_count > right_undecided_right_bracket_num) return;
        if (index == s.size())
        {   
            if (del_times < min_del_times)
            {
                min_del_times = del_times;
                res.clear();
            }
            res.insert(cur_string);
        }
        else
        {
            if (s[index] == ')')
            {
                helper(del_times, left_unmatch_left_bracket_count-1, right_undecided_right_bracket_num-1, res, s, index+1, cur_string+s[index]);
                helper(del_times+1, left_unmatch_left_bracket_count, right_undecided_right_bracket_num-1, res, s, index+1, cur_string);
            }
            else if (s[index] == '(')
            {
                helper(del_times, left_unmatch_left_bracket_count+1, right_undecided_right_bracket_num, res, s, index+1, cur_string+s[index]);
                helper(del_times+1, left_unmatch_left_bracket_count, right_undecided_right_bracket_num, res, s, index+1, cur_string);
            }
            else
            {
                helper(del_times, left_unmatch_left_bracket_count, right_undecided_right_bracket_num, res, s, index+1, cur_string+s[index]);
            }
        }
    }
};