#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
    // https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-w-6/
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> res;
        if (words.empty() || s.size() < words[0].size() * words.size())
        {
            return res;
        }
        auto word_size = words[0].size();
        for (size_t i = 0; i < word_size; i++)
        {
            helper(s.substr(i), words, word_size, res, i);
        }
        return res;
    }
    void helper(string s, vector<string>& words, size_t word_size, vector<int>& res, size_t off_set)
    {
        size_t i = 0;
        size_t j = 0;
        unordered_map<string, int> word2count;
        unordered_map<string, int> cur_word2count;
        for (auto word: words)
        {
            word2count[word] += 1;
            cur_word2count[word] = 0;
        }
        auto unmatched_word_count = word2count.size();
        while (j <= s.size() - word_size)
        {
            if (cur_word2count[s.substr(j, word_size)] < word2count[s.substr(j, word_size)])
            {
                cur_word2count[s.substr(j, word_size)]++;
                if (cur_word2count[s.substr(j, word_size)] == word2count[s.substr(j, word_size)]) unmatched_word_count--;
                if(unmatched_word_count == 0)
                {
                    res.push_back(i + off_set);
                    cur_word2count[s.substr(i, word_size)]--;
                    unmatched_word_count++;
                    i += word_size;
                }
                j += word_size;
            }
            else if (cur_word2count[s.substr(j, word_size)] == word2count[s.substr(j, word_size)])
            {
                while (cur_word2count[s.substr(j, word_size)] == word2count[s.substr(j, word_size)])
                {
                    if (cur_word2count[s.substr(i, word_size)]-- == word2count[s.substr(i, word_size)]) unmatched_word_count++;
                    i += word_size;
                }
                cur_word2count[s.substr(j, word_size)]++;
                unmatched_word_count--;
                j += word_size;
            }
            else
            {
                while (i < j)
                {
                    cur_word2count[s.substr(i, word_size)] = 0;
                    i += word_size;
                }
                unmatched_word_count = word2count.size();
                j += word_size;
                i += word_size;
            }
        }
    }
};
