/*
 * @lc app=leetcode id=684 lang=cpp
 *
 * [684] Redundant Connection
 */

// @lc code=start
class Solution {
public:
    int find(vector<int>& parent, int node) {
        if (parent[node] != node) {
            parent[node] = find(parent, parent[node]);
        }
        return parent[node];
    }

    void Union(vector<int>& parent, int u, int v) {
        parent[find(parent, u)] = find(parent, v);
    }

    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        vector<int> parent(n+1);
        for (int i=1; i<n+1; i++) {
            parent[i] = i;
        }
        for (auto& edge: edges) {
            int u = edge[0], v = edge[1];
            if (find(parent, u) == find(parent, v)) return edge;
            Union(parent, u, v);
        }
        return {};

    }
};
// @lc code=end

