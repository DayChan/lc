#include <string>
#include <unordered_set>


using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> bag;
        int length = 0;
        for (auto head = s.begin(), tail = s.begin(); tail != s.end(); tail++)
        {
            if (bag.find(*tail) == bag.end())
            {
                length = length > tail - head + 1 ? length : tail - head + 1;
            }
            else
            {
                do
                {
                    bag.erase(*head);
                    head++;
                } while (*(head - 1) != *tail);
            }
            bag.insert(*tail);
        }
        return length;
    }
};

int main()
{
    Solution s;
    s.lengthOfLongestSubstring("abcabcbb");
}