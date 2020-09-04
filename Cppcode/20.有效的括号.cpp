#include <string>
#include <stack>

using namespace std;
class Solution {
public:
    bool isValid(string s) {
        stack<char> l;
        for (char c : s)
        {
            if (c == '(' or c == '{' or c == '[') l.push(c);
            else if (l.empty()) return false;
            else if ((c == ')' and l.top() == '(') or (c == '}' and l.top() == '{') or (c == ']' and l.top() == '[')) l.pop();
            else return false;
        }
        if (l.empty()) return true;
        else return false;
    }
};