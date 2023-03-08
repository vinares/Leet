import java.util.Collection;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Stack;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    int ptr;

    public String decodeString(String s) {
        LinkedList<String> stack = new LinkedList<>();
        ptr = 0;

        while (ptr < s.length()){
            char cur_char = s.charAt(ptr);
            if (Character.isDigit(cur_char)){
                String digit = getDigit(s);
                stack.addLast(digit);
            } else if (Character.isLetter(cur_char) || cur_char == '[') {
                stack.addLast(String.valueOf(s.charAt(ptr++)));
            } else {
                ptr++;
                LinkedList<String> new_entry = new LinkedList<>();
                while (!"[".equals(stack.peekLast())) {
                    new_entry.addLast(stack.pollLast());
                }
                stack.removeLast();
                Collections.reverse(new_entry);
                int repeat = Integer.parseInt(stack.removeLast());
                String element = getString(new_entry);
                StringBuffer new_element = new StringBuffer();
                for (int i=0; i<repeat; i++){
                    new_element.append(element);
                }
                stack.addLast(new_element.toString());
            }
        }
        return getString(stack);
    }

    public String getString(LinkedList<String> lists){
        StringBuffer ret = new StringBuffer();
        for (String c : lists){
            ret.append(c);
        }
        return ret.toString();
    }

    public String getDigit(String s){
        StringBuffer ret = new StringBuffer();
        while (Character.isDigit(s.charAt(ptr))) {
            ret.append(s.charAt(ptr++));
        }
        return ret.toString();
    }
}
//leetcode submit region end(Prohibit modification and deletion)
