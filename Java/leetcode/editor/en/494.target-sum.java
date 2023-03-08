//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    int ans = 0;

    private void backtrack(int[] nums, int i, int val, int target) {
        if (i == nums.length) {
            if (val == target) {
                ans ++;
            }
            return;
        }

        backtrack(nums, i+1, val+nums[i], target);
        backtrack(nums, i+1, val-nums[i], target);
        return;

    }

    public int findTargetSumWays(int[] nums, int target) {
        int n = nums.length;
        backtrack(nums, 0, 0, target);
        return ans;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
