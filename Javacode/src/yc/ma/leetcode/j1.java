package yc.ma.leetcode;
import java.util.Map;
import java.util.HashMap;

public class j1 {
    public int[] twoSum(int[] nums, int target) {
        int[] solution = new int[2];
        HashMap<Integer, Integer> num2index = new HashMap<>();
        int index1;
        Integer index2;
        for (index1 = 0; index1 < nums.length; index1++) {
            index2 = null;
            index2 = num2index.get(target - nums[index1]);
            if (index2 != null) {
                solution[0] = index1;
                solution[1] = index2;
            }
            else {
                num2index.put(nums[index1], index1);
            }
        }
        return solution;
    }
}
