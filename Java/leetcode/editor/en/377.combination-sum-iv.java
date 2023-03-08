package leetcode.editor.en;/*
 * @lc app=leetcode id=377 lang=java
 *
 * [377] Combination Sum IV
 */

// @lc code=start
class Solution {
    public int combinationSum4(int[] nums, int target) {
        int[] dp = new int[target+1];
        dp[0] = 1;
        for (int i=1; i<target+1; i++){
            int cur = 0;
            for (int num : nums) {
                if (num > i) continue;
                cur += dp[i-num];
            }
            dp[i] = cur;
        }
        return dp[target];
    }
}
// @lc code=end

