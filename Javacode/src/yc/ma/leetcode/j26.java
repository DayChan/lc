package yc.ma.leetcode;

public class j26 {
    public int removeDuplicates(int[] nums) {
        int i = 0, j = 1;
        while (j < nums.length) {
            if (nums[j] != nums[i]) {
                i += 1;
                nums[i] = nums[j];
            }
            j += 1;
        }
        return i + 1;
    }
}
