import java.util.ArrayList;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int magicalString(int n) {
        ArrayList<Integer> ans = new ArrayList<>();
        ans.add(1);
        boolean one = false;
        int counter = 1;
        int index = 1;
        int new_element;

        while (counter < n) {
            new_element = ans.get(ans.size()-1) == 1 ? 2 : 1;
            index ++;

            if (one) {
                counter ++;
                ans.add(new_element);
            } else {
                counter += 2;
                ans.add(new_element);
                ans.add(new_element);
            }

            one = ans.get(index) == 1 ? true : false;
        }
        int result = 0;
        for (int i=0; i<n; i++) {
            if (ans.get(i) == 1)
                result ++;
        }
        return  result;


    }
}
//leetcode submit region end(Prohibit modification and deletion)
