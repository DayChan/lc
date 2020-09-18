#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> char2count;
        unordered_map<char, int> cur_char2count;
        for (char c: t)
        {
            char2count[c] += 1;
            cur_char2count[c] = 0;
        }
        auto unmatched_char_count = char2count.size();
        string minWindow = "";
        size_t minSize = s.size();
        size_t i = 0;
        size_t j = 0;
        while (j < s.size())
        {
            if (char2count.find(s[j]) != char2count.end())
            {
                cur_char2count[s[j]] += 1;
                if (cur_char2count[s[j]] == char2count[s[j]]) unmatched_char_count--;
                if (unmatched_char_count == 0)
                {
                    while (i < s.size())
                    {
                        if (char2count.find(s[i]) == char2count.end()) i++;
                        else if (cur_char2count[s[i]] > char2count[s[i]])
                        {
                            cur_char2count[s[i]]--;
                            i++;
                        }
                        else
                        {
                            break;
                        }
                    }
                    if (j - i + 1 <= minSize)
                    {
                        minSize = j - i + 1;
                        minWindow = s.substr(i, minSize);
                    }
                    cur_char2count[s[i]]--;
                    unmatched_char_count++;
                    i++;
                }
            }
            j++;
        }
        return minWindow; 
    }
};