/*
 * @lc app=leetcode id=110 lang=cpp
 *
 * [110] Balanced Binary Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int checkHeight(TreeNode* node, bool& ans) {
        if (ans == false) return -1;
        if (!node) return 0;
        int lheight = checkHeight(node->left, ans);
        int rheight = checkHeight(node->right, ans);
        if (abs(lheight-rheight) > 1) ans = false;
        return max(lheight, rheight)+1;
    }
    bool isBalanced(TreeNode* root) {
        bool ans = true;
        int a = checkHeight(root, ans);
        return ans;
    }
};
// @lc code=end

