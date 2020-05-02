package yc.ma.leetcode;

public class j11 {
    public int maxArea(int[] height) {
        int maxarea = 0;
        int i = 0, j = height.length - 1;
        while (i < j) {
            maxarea = Math.max(maxarea, Math.min(height[i], height[j]) * (j - i));
            if (height[i] < height[j]) {
                i += 1;
            }
            else {
                j -= 1;
            }
        }
        return maxarea;
    }
}
