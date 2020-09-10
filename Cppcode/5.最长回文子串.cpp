#include <string>
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<vector<int>> dp;

    string longestPalindrome(string s) {
        auto length = s.size();

        dp = vector<vector<int>> (length, vector<int>(length, 0));

        decltype(length) max_palindrome_length = 0;
        decltype(length) head = 0;
        for (decltype(length) j = 0; j < length; j++)
        {
            for (decltype(length) i = 0; i <= j; i++)
            {
                if (s[i] != s[j])
                {
                    dp[i][j] = -1;
                }
                else
                {
                    if (i == j - 1 || i == j)
                    {
                        dp[i][j] = 1;
                    }
                    else
                    {
                        dp[i][j] = dp[i+1][j-1];
                    }
                }
                if (dp[i][j] == 1 && j - i + 1 > max_palindrome_length)
                {
                    max_palindrome_length = j - i + 1;
                    head = i;
                }
            }
        }
        return s.substr(head, max_palindrome_length);
    }
};