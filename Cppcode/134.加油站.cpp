#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        vector<int> debet(gas.size(), 0);
        decltype(gas.size()) start = 0;
        int extra_gas;
        while (true)
        {
            auto cur_gas = 0;
            auto i = start;
            while (cur_gas >= 0 && i < gas.size())
            {
                cur_gas += gas[i];
                cur_gas -= cost[i];
                i++;
            }
            if (i == gas.size())
            {
                extra_gas = cur_gas;
                break;
            }
            debet[start] = cur_gas;
            start = i;
        }
        if (extra_gas + accumulate(debet.begin(), debet.end(), 0) >= 0)
        {
            return start;
        }
        return -1;
    }
};