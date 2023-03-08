package leetcode.editor.en;/*
 * @lc app=leetcode id=375 lang=java
 *
 * [375] Guess Number Higher or Lower II
 */

// @lc code=start

// Memory Search O(n^3)
class Solution {
    static int N = 202;
    static int[][] memory = new int[N][N];
    
    public int getMoneyAmount(int n) {
        return dfs(1, n);
    }
    
    int dfs(int l, int r){
        if (l >= r) return 0;
        if (memory[l][r] != 0) return memory[l][r];
        int ans = 0x3f3f3f3f;
        for (int x=l; x<=r; x++){
            int cur = Math.max(dfs(l, x-1), dfs(x+1, r)) + x;
            ans = Math.min(ans, cur);
        }
        memory[l][r] = ans;
        return ans;
    }
}

// @lc code=end

