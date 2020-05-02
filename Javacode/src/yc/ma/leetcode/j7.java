package yc.ma.leetcode;

public class j7 {
    public int reverse(int x) {
        int plus = 1;
        if (x < 0) {
            x = -1 * x;
            plus = -1;
        }
        int sum = 0;
        int temp;
        for (temp = x; temp > 0; temp /= 10) {
            if (sum > Integer.MAX_VALUE/10) {
                return 0;
            }
            sum *= 10;
            sum += temp % 10;
        }
        return plus * sum;
    }
}
