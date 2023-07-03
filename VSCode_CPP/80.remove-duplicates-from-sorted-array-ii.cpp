/*
 * @lc app=leetcode id=80 lang=cpp
 *
 * [80] Remove Duplicates from Sorted Array II
 */

// @lc code=start
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int fast = 0;
        int slow = 0;
        int prev = nums[0] - 1;
        int prev_prev = nums[0] - 2;

        for (fast; fast<nums.size(); fast++){
            if (nums[fast] > prev) {
                nums[slow] = nums[fast];
                slow ++;
            }
            else if (nums[fast] == prev)  {
                if (prev_prev < prev) {
                    prev_prev = prev;
                    nums[slow] = nums[fast];
                    slow ++;
                }
            }
            prev = nums[fast];
        }
        return slow;

    }
};
// @lc code=end

