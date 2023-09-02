/*
 * @lc app=leetcode id=72 lang=cpp
 *
 * [72] Edit Distance
 */

// @lc code=start
class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.size(), n = word2.size();
        vector<vector<int>> distance = vector(m+1, vector<int>(n+1, m+n));
        for (int i=0; i<m+1; i++) distance[i][0] = i;
        for (int j=0; j<n+1; j++) distance[0][j] = j;
        for (int i=1; i<m+1; i++) {
            for (int j=1; j<n+1; j++) {
                distance[i][j] = min(distance[i-1][j], distance[i][j-1]) + 1;
                if (word1[i-1] == word2[j-1]) distance[i][j] = min(distance[i][j], distance[i-1][j-1]);
                else distance[i][j] = min(distance[i][j], distance[i-1][j-1]+1);
            }
        }
        return distance[m][n];
    }
};
// @lc code=end

