package leetcode.editor.en;/*
 * @lc app=leetcode id=374 lang=java
 *
 * [374] Guess Number Higher or Lower
 */

// @lc code=start
/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int left = 1, right = n, mid = (int) (n+1)/2;
        
        while (left < right) {
            mid = left + (right-left)/2;
            switch(guess(mid)){
                case 0:
                    return mid;
                case 1:
                    left = mid+1;
                    break;
                default:
                    right = mid-1;
                    break;
            }
        }
        return left;
    }
}
// @lc code=end

