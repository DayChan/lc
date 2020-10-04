#include <vector>

using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.size() == 0)
        {
            return false;
        }
        return binarySearchMatrix(matrix, target, make_pair(0, 0), make_pair(matrix.size()-1, matrix[0].size()-1));
    }

    bool binarySearchMatrix(vector<vector<int>>& matrix, int target, pair<int, int> head, pair<int, int> tail)
    {
        if (head.first > tail.first || head.second > tail.second || target < matrix[head.first][head.second] || target > matrix[tail.first][tail.second])
        {
            return false;
        }
        auto mid = make_pair((head.first+tail.first)/2, (head.second+tail.second)/2);
        if (target == matrix[mid.first][mid.second])
        {
            return true;
        }
        else if (target < matrix[mid.first][mid.second])
        {
            return binarySearchMatrix(matrix, target, head, make_pair(mid.first-1, mid.second-1))
                || binarySearchMatrix(matrix, target, make_pair(mid.first, head.second), make_pair(tail.first, mid.second-1))
                || binarySearchMatrix(matrix, target, make_pair(head.first, mid.second), make_pair(mid.first-1, tail.second));
        }
        else
        {
            return binarySearchMatrix(matrix, target, make_pair(mid.first+1, mid.second+1), tail)
                || binarySearchMatrix(matrix, target, make_pair(mid.first+1, head.second), make_pair(tail.first, mid.second))
                || binarySearchMatrix(matrix, target, make_pair(head.first, mid.second+1), make_pair(mid.first, tail.second));
        }
    }
};