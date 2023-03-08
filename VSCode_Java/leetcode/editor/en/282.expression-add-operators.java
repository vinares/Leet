import java.util.ArrayList;
import java.util.List;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    List<String> ans;
    int n;
    int target;
    String num;

    public void backTrack(StringBuffer expr, int i, long res, long mul){
        if (i==n){
            if(res==target){
                ans.add(expr.toString());
            }
            return;
        }
        int signIndex = expr.length();
        if(i>0){
            expr.append(0);
        }
        long val = 0;
        for (int j=i; j<n && (j==i || num.charAt(i)!='0'); ++j) {
            val = val * 10 + num.charAt(j)-'0';
            expr.append(num.charAt(j));
            if(i==0){
                backTrack(expr, j+1, val, val);
            } else {
                expr.setCharAt(signIndex, '+');
                backTrack(expr,j+1,res+val, val);
                expr.setCharAt(signIndex, '-');
                backTrack(expr, j+1, res-val, -val);
                expr.setCharAt(signIndex, '*');
                backTrack(expr, j+1, res-mul + mul*val, mul*val);
            }
        }
        expr.setLength(signIndex);
    }

    public List<String> addOperators(String num, int target) {
        this.n = num.length();
        this.num = num;
        this.target = target;
        this.ans = new ArrayList<String>();
        StringBuffer expr = new StringBuffer();
        backTrack(expr, 0, 0, 0);
        return ans;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
