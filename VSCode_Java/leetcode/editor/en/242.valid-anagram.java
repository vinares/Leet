package leetcode.editor.en;/*
 * @lc app=leetcode id=242 lang=java
 *
 * [242] Valid Anagram
 */

// @lc code=start
import java.util.*;
class Solution {
    public boolean isAnagram(String s, String t) {
        int[] mem = new int[26];
        for (char c : s.toCharArray()) {
            mem[c - 'a']++;
        }
        for (char c : t.toCharArray()) {
            mem[c - 'a']--;
        }
        for (int n : mem) {
            if (n != 0)
                return false;
        }
        return true;
    }
}
// @lc code=end

