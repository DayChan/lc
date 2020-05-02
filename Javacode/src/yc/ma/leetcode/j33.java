package yc.ma.leetcode;

public class j33 {
    public int search(int[] nums, int target) {
        if (nums.length == 0) {
            return -1;
        }
        if (nums.length == 1) {
            if (nums[0] == target) {
                return 0;
            }
            return -1;
        }
        int left = nums[0], right = nums[nums.length - 1];
        int start = 0, end = (nums.length - 1), mid;
        if (target >= left) {
            // target is on the left
            while (start <= end && nums[start] >= left) {
                mid = (start + end) / 2;
                if (nums[mid] < left) {
                    end = mid - 1;
                }
                else {
                    if (nums[mid] == target) {
                        return mid;
                    }
                    else if (nums[mid] < target) {
                        start = mid + 1;
                    }
                    else {
                        end = mid - 1;
                    }
                }
            }
        }
        else {
            //target is on the right
            while (start <= end && nums[end] <= right) {
                mid = (start + end) / 2;
                if (nums[mid] > right) {
                    start = mid + 1;
                }
                else {
                    if (nums[mid] == target) {
                        return mid;
                    }
                    else if (nums[mid] < target) {
                        start = mid + 1;
                    }
                    else {
                        end = mid - 1;
                    }
                }
            }
        }
        return -1;
    }
}
