class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {}
        d["2"] = ["a", "b", "c"]
        d["3"] = ["d", "e", "f"]
        d["4"] = ["g", "h", "i"]
        d["5"] = ["j", "k", "l"]
        d["6"] = ["m", "n", "o"]
        d["7"] = ["p", "q", "r", "s"]
        d["8"] = ["t", "u", "v"]
        d["9"] = ["w", "x", "y", "z"]
        l = list(digits)
        res = []
        s = ""
        self.helper(l, d, s, res)
        return res

    def helper(self, l, d, s, res):
        if len(l) == 0:
            if len(s) != 0:
                res.append(s)
            return
        n = l[0]
        for c in d[n]:
            news = s[:]
            news += c
            self.helper(l[1:], d, news, res) 
            