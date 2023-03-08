package leetcode.editor.en;/*
 * @lc app=leetcode id=389 lang=java
 *
 * [389] Find the Difference
 */

// @lc code=start
class Solution {
    public char findTheDifference(String s, String t) {
        int[] ht = new int[26];
        Arrays.fill(ht, 0);
        for (int i=0; i<s.length(); i++) 
            ht[(int) s.charAt(i)- 'a'] ++;
        for (int j=0; j<t.length(); j++){
            int i = (int) t.charAt(j) - 'a';
            ht[i]--;
            if (ht[i] < 0){
                return (char) (i + (int) 'a');
            }
        }
        return 'a';
    }
}
// @lc code=end

