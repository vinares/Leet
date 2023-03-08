package leetcode.editor.en;/*
 * @lc app=leetcode id=16 lang=java
 *
 * [16] 3Sum Closest
 */

// @lc code=start
class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        var best = 0;

        for (int i=0, n=nums.length, mindiff=Integer.MAX_VALUE; i<n-2; i++){
            for (int j=i+1, k=n-1; j<k;) {
                var sum = nums[i] + nums[j] + nums[k];
                if (sum == target)
                    return target;
                if (sum < target)
                    j ++;
                else
                    k --;
                var diff = Math.abs(target-sum);
                if (diff < mindiff){
                    mindiff = diff;
                    best = sum;
                }
            }
        }
        return best;
    }
}
// @lc code=end

