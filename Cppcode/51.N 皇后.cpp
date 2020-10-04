#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        unordered_set<int> col_index;
        unordered_set<int> iplusj;
        unordered_set<int> iminusj;
        vector<vector<string>> res;
        vector<string> resEntry;
        helper(n, col_index, iplusj, iminusj, res, resEntry, 0);
        return res;
    }

    void helper(int n, unordered_set<int>& col_index, unordered_set<int>& iplusj, unordered_set<int>& iminusj, vector<vector<string>>& res, vector<string> resEntry, int i)
    {
        if (i == n)
        {
            res.push_back(resEntry);
        }
        for (auto j = 0; j < n; j++)
        {
            if (col_index.count(j) == 0 && iplusj.count(i+j) == 0 && iminusj.count(i-j) == 0)
            {
                col_index.insert(j);
                iplusj.insert(i+j);
                iminusj.insert(i-j);
                auto s = string();
                for (auto t = 0; t < n; t++)
                {
                    if (t == j) s += "Q";
                    else s += ".";
                }
                resEntry.push_back(s);
                helper(n, col_index, iplusj, iminusj, res, resEntry, i+1);
                resEntry.pop_back();
                iminusj.erase(i-j);
                iplusj.erase(i+j);
                col_index.erase(j);
            }
        }
    }
};