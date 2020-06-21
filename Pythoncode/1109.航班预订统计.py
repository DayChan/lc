class Solution:
    """
    https://leetcode-cn.com/problems/corporate-flight-bookings/solution/qian-zhui-he-fa-python-java-shi-jian-fu-za-du-on-b/
    """
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0]*n
        for l, r, seat in bookings:
            res[l - 1] += seat
            if r < n:
                res[r] -= seat
        for i in range(1,n):
            res[i] += res[i - 1]
        return res

