class Solution:
    def restoreIpAddresses(self, s: str):
        res = []
        self.helper("", 0, s, res)
        return res

    def helper(self, ip, counter, s, res):
        if counter > 4:
            return
        elif counter == 4:
            if len(s) == 0:
                res.append(ip)
        else:
            if len(s) > 3 * (4 - counter):
                return
            for i in range(min(3, len(s))):
                if int(s[:i+1]) <= 255:
                    if len(s[:i+1]) > 1 and s[:i+1][0] == "0": #不能以0开头
                        continue
                    newip = ip[:]
                    newip += s[:i+1]
                    newcounter = counter
                    newcounter += 1
                    if newcounter < 4:
                        newip += "."
                    self.helper(newip, newcounter, s[i+1:], res)