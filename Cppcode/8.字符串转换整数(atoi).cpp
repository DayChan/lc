#include <string>
#include <climits>
#include <unordered_set>

using namespace std;
class Solution {
public:
    int myAtoi(string str) {
        int res = 0;
        int np;
        unordered_set<char> numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
        auto index = str.find_first_not_of(' ');
        if (index == string::npos || (numbers.find(str[index]) == numbers.end() && str[index] != '+' && str[index] != '-'))
        {
            return 0;
        }
        if (str[index] == '-')
        {
            np = -1;
            index++;
        }
        else if (str[index] == '+')
        {
            np = 1;
            index++;
        }
        else
        {
            np = 1;
        }
        while (index < str.size() && numbers.find(str[index]) != numbers.end())
        {
            int pop = stoi(string(1, str[index])) * np;
            if (res > INT_MAX/10 || (res == INT_MAX / 10 && pop > 7)) return INT_MAX;
            if (res < INT_MIN/10 || (res == INT_MIN / 10 && pop < -8)) return INT_MIN;
            res = res * 10 + pop;
            index++;
        }
        return res;
    }
};