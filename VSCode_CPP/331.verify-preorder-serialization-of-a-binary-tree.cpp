/*
 * @lc app=leetcode id=331 lang=cpp
 *
 * [331] Verify Preorder Serialization of a Binary Tree
 */

// @lc code=start
class Solution {
public:
    bool isValidSerialization(string preorder) {
        int i = 0;
        int leaves = 1;
        while (i<preorder.size()) {
            if (leaves == 0) return false;
            if (preorder[i] == ',') i++;
            else if (preorder[i] == '#') {
                i++;
                leaves--;
            } else {
                while (i<preorder.size() && preorder[i] != ',') i++;
                leaves++;
            }
        }
        return leaves == 0;
    }
};
// @lc code=end

