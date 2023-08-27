/*
 * @lc app=leetcode id=1171 lang=cpp
 *
 * [1171] Remove Zero Sum Consecutive Nodes from Linked List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
   public:
    ListNode* removeZeroSumSublists(ListNode* head) {
        unordered_map<int, ListNode*> mem;
        int sum = 0;
        ListNode* dummy = new ListNode(0, head);
        for (ListNode* node = dummy; node; node = node->next) {
            sum += node->val;
            mem[sum] = node;
        }
        sum = 0;
        for (ListNode* node = dummy; node; node = node->next) {
            sum += node->val;
            node->next = mem[sum]->next;
        }
        return dummy->next;
    }
};
// @lc code=end
