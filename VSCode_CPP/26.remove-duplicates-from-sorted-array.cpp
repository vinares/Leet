/*
 * @lc app=leetcode id=26 lang=cpp
 *
 * [26] Remove Duplicates from Sorted Array
 */

// @lc code=start
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int slow = 0;
        int fast = 0;
        int prev = nums[0]-1;
        for (fast; fast<nums.size(); fast++){
            if (nums[fast] > prev){
                nums[slow] = nums[fast];
                slow ++;
            }
            prev = nums[fast];
        }
        return slow;

    }
};
// @lc code=end

