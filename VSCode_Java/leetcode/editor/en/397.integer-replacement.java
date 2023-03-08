//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int integerReplacement(int n) {
        int ans = 0;
        while (n > 1){
            if((n & 1) == 0){
                n >>= 1;
                ans += 1;
            } else if (n == 3) {
                ans += 2;
                n = 1;
            } else if ((n & 3) == 3) {
                n = n / 2 +1;
                ans += 2;
            } else {
                n = n/2 ;
                ans += 2;
            }
        }
        return ans;
    }
}

//leetcode submit region end(Prohibit modification and deletion)
