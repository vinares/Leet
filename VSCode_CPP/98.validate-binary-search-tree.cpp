/*
 * @lc app=leetcode id=98 lang=cpp
 *
 * [98] Validate Binary Search Tree
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
    bool isValid(TreeNode* root, long long int l, long long int r) {
        if (root == nullptr) return true;
        if (root->val < r and root->val > l) 
            return isValid(root->left, l, root->val) and isValid(root->right, root->val, r);
        return false;
    }

    bool isValidBST(TreeNode* root) {
        long long int l = -2147483648, r = 2147483647;
        cout << l << endl;
        return isValid(root, l, r);
    }
};
// @lc code=end

