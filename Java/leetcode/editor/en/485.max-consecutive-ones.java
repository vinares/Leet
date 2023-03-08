//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int max_one = 0;
        int cur_one = 0;
        for (int num : nums) {
            if (num == 1) {
                cur_one += 1;
                max_one = Math.max(cur_one, max_one);
            } else cur_one = 0;
        }
        return max_one;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
