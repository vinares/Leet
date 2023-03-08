import java.util.Stack;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        Stack<Integer> stack = new Stack<Integer>();
        int[] answer = new int[n];

        for(int i=0; i<n; i++) {
            answer[i] = -1;
        }

        for (int i=0; i<2*n-1; i++){
            while(!stack.empty() && nums[stack.lastElement()] < nums[i%n]) {
                answer[stack.pop()] = nums[i%n];
            }
            stack.add(i%n);
        }

        return answer;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
