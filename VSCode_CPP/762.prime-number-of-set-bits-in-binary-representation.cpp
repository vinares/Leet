/*
 * @lc app=leetcode id=762 lang=cpp
 *
 * [762] Prime Number of Set Bits in Binary Representation
 */

// @lc code=start
class Solution {
public:
    int countPrimeSetBits(int left, int right) {
        int ans = 0;
        // 2，3，5，7，11，13，17，19
        int mask = 0b10100010100010101100;
        for (int i=left; i<=right; i++){
            if (1 << __builtin_popcount(i) & mask)
                ans++;
        }
        return ans;
    }
};
// @lc code=end

