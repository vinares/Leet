//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public String licenseKeyFormatting(String s, int k) {
        StringBuffer strbff = new StringBuffer();
        int pointer = s.length()-1;
        StringBuffer curstr = new StringBuffer();
        char cur_c;
        for (int i=s.length()-1; i>=0; i--){
            if (s.charAt(i) == '-')
                continue;
            cur_c = Character.toUpperCase(s.charAt(i));
            curstr.append(cur_c);
            if (curstr.length() == k) {
                strbff.append(curstr);
                strbff.append('-');
                curstr.delete(0, curstr.length());
            }
        }
        if (curstr.length() > 0) {
            strbff.append(curstr);
        } else {
            if (strbff.length()>-0)
                strbff.delete(strbff.length()-1,strbff.length());
        }
        String result = strbff.reverse().toString();
        return result;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
