#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<char>> n2chars;

    vector<string> letterCombinations(string digits) {
        vector<string> res;
        if (digits == "") return res;
        n2chars = { 
                    {},
                    {},
                    {'a', 'b', 'c'},
                    {'d', 'e', 'f'},
                    {'g', 'h', 'i'},
                    {'j', 'k', 'l'},
                    {'m', 'n', 'o'},
                    {'p', 'q', 'r', 's'},
                    {'t', 'u', 'v'},
                    {'w', 'x', 'y', 'z'}
                  };
        helper(res, digits, "");
        return res;
    }

    void helper(vector<string> &res, string digits, string cur_string)
    {
        if (digits == "")
        {
            res.push_back(cur_string);
        }
        else
        {
            for (char c : n2chars[stoi(string(1, digits.front()))])
            {
                helper(res, digits.substr(1), cur_string + c);
            }
        }
    }
};