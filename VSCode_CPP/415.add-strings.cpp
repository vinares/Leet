/*
 * @lc app=leetcode id=415 lang=cpp
 *
 * [415] Add Strings
 */

// @lc code=start
class Solution {
public:
    string addStrings(string num1, string num2) {
        vector<char> digits;
        int p1 = num1.size()-1, p2 = num2.size()-1;
        int flag = 0;
        int val_1 = 0, val_2 = 0;
        int sum = 0;
        
        while (p1 >= 0 || p2 >= 0) {
            if (p1 >= 0) {
                val_1 = num1[p1] - '0';
                p1--;
            } else val_1 = 0;
            if (p2 >= 0) {
                val_2 = num2[p2] - '0';
                p2 --;
            } else val_2 = 0;
            sum = val_1 + val_2 + flag;
            flag = (sum > 9);
            sum -= (flag * 10);
            digits.push_back('0'+sum);
        }
        for (auto x:digits) {
            cout << x <<endl;
        }
        if (flag > 0) {
            digits.push_back('1');
        }
        string ans;
        for (int i=digits.size()-1; i>-1; i--) {
            ans += digits[i];
        }
        return ans;
    }
};
// @lc code=end

