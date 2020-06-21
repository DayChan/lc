class Solution:
    """
    https://leetcode-cn.com/problems/candy/solution/candy-cong-zuo-zhi-you-cong-you-zhi-zuo-qu-zui-da-/
    """
    def candy(self, ratings: List[int]) -> int:
        left = [1 for _ in range(len(ratings))]
        right = [1 for _ in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i + 1]: right[i] = right[i + 1] + 1
        count = sum([max(r, l) for r, l in zip(right, left)])
        return count

