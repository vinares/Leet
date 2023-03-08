import java.util.ArrayList;
import java.util.Arrays;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int findRotateSteps(String ring, String key) {
        int m=ring.length(), n=key.length();
        List<Integer>[] alphabet = new List[26];
        for (int i=0; i<26; i++){
            alphabet[i] = new ArrayList<Integer>();
        }
        for (int i=0; i<m; i++){
            alphabet[ring.charAt(i)-'a'].add(i);
        }
        int[][] dp = new int[n][m];
        for (int i=0; i<n; i++) {
            Arrays.fill(dp[i], 0x3f3f3f3f);
        }

        for (int pos : alphabet[key.charAt(0)-'a']) {
            dp[0][pos] = Math.min(pos, m-pos) + 1;
        }
        for (int i=1; i<n; i++) {
            for (int j: alphabet[ring.charAt(i)-'a']) {
                for (int k: alphabet[ring.charAt(i-1)-'a']) {
                    dp[i][j] = Math.min(dp[i][j], dp[i-1][k] + 1 + Math.min(Math.abs(k-j), m-Math.abs(k-j)));
                }
            }
        }

        return Arrays.stream(dp[n-1]).min().getAsInt();

    }
}
//leetcode submit region end(Prohibit modification and deletion)
