/*
 * @lc app=leetcode id=235 lang=cpp
 *
 * [235] Lowest Common Ancestor of a Binary Search Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    void dfs_parent(TreeNode* root, unordered_map<TreeNode*, TreeNode*>& parent) {
        if (!root) return;
        if (root->left) parent[root->left] = root;
        if (root->right) parent[root->right] = root;
        dfs_parent(root->left, parent);
        dfs_parent(root->right, parent);
        return;
    }

    TreeNode* parent_map(TreeNode* root, TreeNode* p, TreeNode* q) {
        unordered_map<TreeNode*, TreeNode*> parent;
        parent[root] = nullptr;
        dfs_parent(root, parent);
        int p_height = 0;
        TreeNode* pp = p;
        while (pp != root) {
            pp = parent[pp];
            p_height++;
        }
        int q_height = 0;
        TreeNode* qp = q;
        while (qp != root) {
            qp = parent[qp];
            q_height++;
        }
        while (p_height > q_height) {
            p = parent[p];
            p_height--;
        }
        while (q_height > p_height) {
            q = parent[q];
            q_height--;
        }
        while (p != q) {
            p=parent[p];
            q=parent[q];
        }
        return p;
    }

    TreeNode* BSTrecursion(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (!root) return root;
        if (root->val>p->val && root->val>q->val) return BSTrecursion(root->left, p, q);
        if (root->val<p->val && root->val<q->val) return BSTrecursion(root->right, p, q);
        return root;
    }

    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        return BSTrecursion(root, p, q);
    }
};
// @lc code=end

