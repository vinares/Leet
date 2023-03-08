import java.util.ArrayList;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {

    public boolean PredictTheWinner(int[] nums) {
        int n = nums.length;
        int player = n % 2 == 1 ? 1 : -1;
        int [][] dp = new int[n][n];
        int left, right;
        for (int len=0; len<n; len++) {
            for(left=0; left+len<n; left ++) {
                right = left + len;
                if (len==0) {
                    dp[left][right] = nums[left] * player;
                    continue;
                }
                if (player > 0) {
                    dp[left][right] = Math.max(dp[left+1][right]+nums[left], dp[left][right-1]+nums[right]);
                } else {
                    dp[left][right] = Math.min(dp[left + 1][right] - nums[left], dp[left][right-1] - nums[right]);
                }
            }
            player *= -1;
        }

        return dp[0][n-1] >= 0;

    }
}
//leetcode submit region end(Prohibit modification and deletion)
