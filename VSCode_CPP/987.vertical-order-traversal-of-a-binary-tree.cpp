/*
 * @lc app=leetcode id=987 lang=cpp
 *
 * [987] Vertical Order Traversal of a Binary Tree
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
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        vector<vector<int>> ans;
        ans.push_back(vector<int>());
        queue<pair<int, TreeNode*>> q;
        if (root) q.push(make_pair(0, root));
        int left_off=0, right_off=0;
        while (!q.empty()) {
            int qlen = q.size();
            int left_max=left_off, right_max=right_off;
            vector<vector<int>> tmp(right_off-left_off+1, vector<int>());
            for (int i=0; i<qlen; i++) {
                int index = q.front().first;
                TreeNode* node = q.front().second;
                q.pop();
                tmp[index-left_off].push_back(node->val);
                if (node->left) {
                    q.push(make_pair(index-1, node->left));
                    left_max=min(left_max, index-1);
                }
                if (node->right) {
                    q.push(make_pair(index+1, node->right));
                    right_max=max(right_max,index+1);
                }
            }
            for (int i=0; i<tmp.size(); i++) {
                sort(tmp[i].begin(), tmp[i].end());
                ans[i].insert(ans[i].end(), make_move_iterator(tmp[i].begin()), make_move_iterator(tmp[i].end()));
            }
            while (left_off > left_max) {
                ans.insert(ans.begin(), vector<int>());
                left_off--;
            }
            while (right_off < right_max) {
                ans.push_back(vector<int>());
                right_off++;
            }
        }
        return ans;
    }
};
// @lc code=end

