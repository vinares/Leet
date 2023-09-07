/*
 * @lc app=leetcode id=105 lang=cpp
 *
 * [105] Construct Binary Tree from Preorder and Inorder Traversal
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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int p_ptr = 0, i_ptr = 0;
        TreeNode* root = nullptr;
        TreeNode* cur = nullptr;
        stack<TreeNode*> s;
        while (p_ptr<preorder.size()) {
            if (!s.empty() && s.top()->val==inorder[i_ptr]) {
                while (!s.empty() && s.top()->val==inorder[i_ptr]) {
                    cur = s.top();
                    s.pop();
                    i_ptr++;
                }
                TreeNode* new_node = new TreeNode(preorder[p_ptr++]);
                cur->right = new_node;
                cur = new_node;
                s.push(new_node);
            } else {
                TreeNode* new_node = new TreeNode(preorder[p_ptr++]);
                if (!root) {
                    root = new_node;
                } else {
                    cur->left = new_node;
                }
                cur = new_node;
                s.push(cur);
            }        
        }
        return root;
    }
};

// @lc code=end

