/*
 * @lc app=leetcode id=581 lang=cpp
 *
 * [581] Shortest Unsorted Continuous Subarray
 */

// @lc code=start
class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        int n = nums.size();
        if (n<2) return 0;
        vector<int> biggest(n, 0);
        vector<int>smallest(n, n+1);
        for(int i=0; i<n; i++) {
            biggest[i] = nums[i];
            if (i > 0){
                biggest[i] = max(biggest[i], biggest[i-1]);
            }
            smallest[n-i-1] = nums[n-i-1];
            if (n-i-1 < n-1){
                smallest[n-i-1] = min(smallest[n-i-1], smallest[n-i]);
            }
        }

        int left = 0;
        int right = n-1;
        while (left < n-1){
            if (left+1<n && nums[left] <= smallest[left+1]) left ++;
            else break;
        }
        while (right > 0) {
            if (right-1>=0 && nums[right] >= biggest[right-1]) right --;
            else break;
        }
        return max(0, right-left+1);
    }
};
// @lc code=end

