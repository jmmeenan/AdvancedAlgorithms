package Leetcode.java;
import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hold = new HashMap<Integer, Integer>();
        int[] output = new int[2];
        for(int i = 0; i< nums.length; i++){
            if(hold.containsKey(nums[i])){
                output[0] = hold.get(nums[i]);
                output[1] = i;
                break;
            }else{
                hold.put(target-nums[i], i);
            }
        }
        return output;
    }

    //Test cases

    public static void main(String[] args) {
        int[] nums = {2,7,11,15};
        int target = 9;
        Solution sol = new Solution();
        int[] output = sol.twoSum(nums, target);
        System.out.println(output[0] + " " + output[1]);  
    }
}

