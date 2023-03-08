package leetcode.editor.en;/*
 * @lc app=leetcode id=9 lang=java
 *
 * [9] Palindrome Number
 */

// @lc code=start
class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0){
            return false;
        }
        int nums = x;
        int reverse = 0;
        while (x!=0){
            reverse = reverse * 10 + x%10;
            x /= 10;
        }
        return nums == reverse;
    }
}
// @lc code=end

