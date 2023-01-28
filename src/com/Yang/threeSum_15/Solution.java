package com.Yang.threeSum_15;

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List res = new ArrayList();
        for (int i = 0; i < nums.length-2; i++) {
            for (int j = 1; j < nums.length-1; j++) {
                for (int k = 2; k < nums.length; k++) {
                    if (nums[i] + nums[j] + nums[k] == 0){

                    }
                }
            }
        }
        return res;

    }

    public static void main(String[] args) {
        Solution s = (Solution) new Solution().threeSum(new int[]{-1, 0, 1, 2, -1, -4});
        System.out.println(s.toString());
    }
}