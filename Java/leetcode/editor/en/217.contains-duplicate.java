package leetcode.editor.en;/*
 * @lc app=leetcode id=217 lang=java
 *
 * [217] Contains Duplicate
 */

// @lc code=start
import java.util.*;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Hashtable<Integer, Integer> dict = new Hashtable <>();
        for(int i=0;i<nums.length;i++){
            if(dict.get(nums[i])==null)
                dict.put(nums[i], 1);
            else
                return true;
        }
        return false;
    }
}
// @lc code=end

