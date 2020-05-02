package yc.ma.leetcode;

import java.util.List;
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;
import java.util.Map;
import java.util.HashMap;
public class j15 {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> ll = new ArrayList<>();
        Set<Integer> fixednums = new HashSet<>();
        int ai, bi, ci;
        for (ai = 0; ai < nums.length; ai++) {
            if (!fixednums.contains(nums[ai])) {
                Map<Integer, Boolean> num2ifused = new HashMap<>();
                for (bi = ai + 1; bi < nums.length; bi++) {
                    if (!fixednums.contains(nums[bi])) {
                        if (num2ifused.containsKey(-nums[ai] - nums[bi])) {
                            if (!num2ifused.get(-nums[ai] - nums[bi])) {
                                num2ifused.put(-nums[ai] - nums[bi], true);
                                num2ifused.put(nums[bi], true);
                                List<Integer> l = new ArrayList<>();
                                l.add(nums[ai]);
                                l.add(nums[bi]);
                                l.add(-nums[ai] - nums[bi]);
                                ll.add(l);
                            }
                        }
                        else {
                            num2ifused.put(nums[bi], false);
                        }
                    }
                }
            }
            fixednums.add(nums[ai]);
        }
        return ll;
    }
}
