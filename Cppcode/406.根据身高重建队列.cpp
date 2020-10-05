#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool compK(vector<vector<int>> p1, vector<vector<int>> p2)
    {
        return p1[1] < p2[1];
    }
    
    bool compH(vector<vector<int>> p1, vector<vector<int>> p2)
    {
        return p1[0] > p2[0];
    }
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        sort(people.begin(), people.end(), compK);
        stable_sort(people.begin(), people.end(), compH);
        vector<vector<int>> res;
        for (auto iter = people.begin(); iter < people.end(); iter++)
        {
            res.insert(res.begin()+(*iter)[1], *iter);
        }
        return res;
    }
};