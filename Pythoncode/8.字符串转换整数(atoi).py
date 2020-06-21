class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MIN = - 2**31
        INT_MAX = 2**31 - 1
        if not str.split():
            return 0
        s = str.split()[0]
        try:
            number = int(s)
        except ValueError:
            numberSet2 = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", "+"])
            numberSet = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
            if s[0] not in numberSet2:
                number =  0
            else:
                i = 1
                for i in range(1, len(s)):
                    if s[i] not in numberSet:
                        break
                try:
                    number = int(s[:i])
                except ValueError:
                    number = 0

        if number < INT_MIN:
            return INT_MIN
        elif number > INT_MAX:
            return INT_MAX
        else:
            return number