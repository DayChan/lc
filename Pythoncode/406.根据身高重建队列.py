class Solution:
    def reconstructQueue(self, people):
        people.sort(key=lambda x: x[1], reverse=True)
        people.sort(key=lambda x: x[0]) # python sort is stable, 经过这两次sort，people变成按h从小到大排列，相同的h按k从大到小排列
        res = [None for _ in range(len(people))]
        noneindex = [i for i in range(len(res))] # noneindex里的元素，代表res里边值为None的index
        for n, k in people:
            index = noneindex.pop(k) #前面应该有k个None
            res[index] = [n, k]
        return res


s = Solution()
s.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])