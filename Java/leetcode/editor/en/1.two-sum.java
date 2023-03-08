package leetcode.editor.en;/*
 * @lc app=leetcode id=1 lang=java
 *
 * [1] Two Sum
 */

// @lc code=start
import java.util.*;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> mem = new HashMap<>();
        for(int i=0; i < nums.length; i++){
            if(mem.containsKey(nums[i])){
                int left = mem.get(nums[i]);
                return new int[]{left, i};
            }
            else
                mem.put(target-nums[i], i);
        }
        return new int[2];
    }
}
// @lc code=end

