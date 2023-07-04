/*
 * @lc app=leetcode id=316 lang=cpp
 *
 * [316] Remove Duplicate Letters
 */

// @lc code=start
class Solution {
public:
    string removeDuplicateLetters(string s) {
        vector<int> last_locs(26, 0);
        vector<bool> seen(26, false);
        for (int i=0; i<s.size(); i++){
            last_locs[s[i]-'a'] = i;
        }
        stack<char> st;
        string ans = "";
        for (int i=0; i<s.length(); i++){
            int cur_p = s[i] - 'a';
            if (seen[cur_p]) continue;
            while(st.size()>0 && s[i]<st.top() && i < last_locs[st.top()-'a']) {
                seen[st.top()-'a'] = false;
                st.pop();
            }
            st.push(s[i]);
            seen[cur_p] = true;
        }
        while (!st.empty()){
            ans = st.top() + ans;
            st.pop();
        }
        return ans;
    }
};
// @lc code=end

