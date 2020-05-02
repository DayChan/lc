package yc.ma.leetcode;

public class j4 {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        /**
         * https://leetcode.com/articles/median-of-two-sorted-arrays/
         */
        if(nums1.length>nums2.length) return  findMedianSortedArrays(nums2,nums1);
        int m = nums1.length;
        int n = nums2.length;
        int left = 0;
        int right = m;

        int i;
        int j;

        while(left<=right){
            i = left+(right-left)/2;
            j = (m+n+1)/2-i;
            double leftAmax = (i==0)?Integer.MIN_VALUE:nums1[i-1];
            double leftBmax = (j==0)?Integer.MIN_VALUE:nums2[j-1];
            double rightAmin = (i==m)?Integer.MAX_VALUE:nums1[i];
            double rightBmin = (j==n)?Integer.MAX_VALUE:nums2[j];
            if(leftAmax>rightBmin){
                right = i-1;
            }else if(leftBmax > rightAmin){
                left = i+1;
            }else{
                if((m+n)%2 == 0){
                    return (Math.max(leftAmax,leftBmax)+Math.min(rightAmin,rightBmin))/2;
                }else{
                    return Math.max(leftAmax,leftBmax);

                }
            }
        }
        return -1;
    }
    public double findMedianSortedArrays2(int[] nums1, int[] nums2) {
        if (nums1.length == 0) {
            return findPosition(nums2, nums1, 0, 0);
        }
        else if (nums2.length == 0) {
            return findPosition(nums1, nums2, 0, 0);
        }
        else if (nums1[0] <= nums2[0]) {
            return findPosition(nums1, nums2, 0, 0);
        }
        else {
            return findPosition(nums2, nums1, 0, 0);
        }
    }
    private double findPosition(int[] nums1, int[] nums2, int i, int j) {
        double returnValue;
        int nums2jPositionInnums1, numOfItembeforenums2j;

        if (j == nums2.length) {
            nums2jPositionInnums1 = nums1.length;
        }
        else {
            nums2jPositionInnums1 = binarySearchOff1(nums1, i, nums2[j]);
        }
        numOfItembeforenums2j = j + nums2jPositionInnums1;
        if (numOfItembeforenums2j < (nums1.length + nums2.length) / 2) {
            returnValue = findPosition(nums2, nums1, j + 1, nums2jPositionInnums1);
        }
        else {
            if ((nums1.length + nums2.length) % 2 == 0) {
                if (numOfItembeforenums2j == (nums1.length + nums2.length) / 2) {
                    returnValue = ((float)nums2[j] + nums1[nums2jPositionInnums1-1]) / 2;
                }
                else {
                    int offset = numOfItembeforenums2j - (nums1.length + nums2.length) / 2;
                    returnValue = ((float)nums1[nums2jPositionInnums1 - offset] + nums1[nums2jPositionInnums1 - offset - 1]) / 2;
                }
            }
            else {
                if (numOfItembeforenums2j == (nums1.length + nums2.length) / 2) {
                    returnValue = nums2[j];
                }
                else {
                    int offset = numOfItembeforenums2j - (nums1.length + nums2.length) / 2;
                    returnValue = nums1[nums2jPositionInnums1 - offset];
                }
            }
        }
        return returnValue;
    }
    private int binarySearchOff1(int[] nums, int head, int target) {
        int start = head, end = nums.length - 1;
        int mid = (start + end) / 2;

        while (mid >= start && mid <= end) {
            if (nums[mid] == target) {
                return mid +1;
            }
            else if (nums[mid] > target) {
                end = mid - 1;
                mid = (start + end) / 2;
            }
            else {
                start = mid + 1;
                mid = (start + end) / 2;
            }
        }

        if (nums[mid] > target) {
            return mid - 1;
        }
        else {
            return mid + 1;
        }
    }


}
