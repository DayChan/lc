package yc.ma.leetcode;

public class j41 {
    public int firstMissingPositive(int[] nums) {
        /**
         * https://blog.csdn.net/Jin_Kwok/article/details/51039381
         */
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] >= 1 && nums[i] <= nums.length) {
                int tmp1 = nums[nums[i] - 1];
                int tmp2 = nums[i];
                nums[nums[i] - 1] = nums[i];
                nums[i] = tmp1;
                if (tmp1 != tmp2) {
                    i--;
                }
            }
        }
        int i = 0;
        for (; i < nums.length; i++) {
            if (nums[i] != i + 1) {
                break;
            }
        }
        return i + 1;
    }
}
