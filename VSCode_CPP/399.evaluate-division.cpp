/*
 * @lc app=leetcode id=399 lang=cpp
 *
 * [399] Evaluate Division
 */

// @lc code=start
class Solution {
private:        
    vector<int> uf;
    vector<double> weight;
    int find(int vertex) {
        if (uf[vertex]!=vertex) {
            int parent = find(uf[vertex]);
            weight[vertex] = weight[vertex] * weight[uf[vertex]];
            uf[vertex] = parent;
        }
        return uf[vertex];
    }
    void unite(int v_from, int v_to, double value) {
        int v_from_parent = find(v_from);
        int v_to_parent = find(v_to);
        uf[v_from_parent] = v_to_parent;
        weight[v_from_parent] = value * weight[v_to] / weight[v_from];
    }

    vector<double> union_find(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        unordered_map<string, int> vertices;
        int ver_count = 0;
        for (int i=0; i<equations.size(); i++) {
            for (int j=0; j<equations[i].size(); j++) {
                if (vertices.find(equations[i][j]) == vertices.end()) vertices[equations[i][j]] = ver_count++;
            }
        }
        uf.resize(ver_count);
        weight.resize(ver_count, 1.0);
        for (int i=0; i<ver_count; i++) uf[i] = i;
        for (int i=0; i<equations.size(); i++) {
            int v_from = vertices[equations[i][0]], v_to = vertices[equations[i][1]];
            unite(v_from, v_to, values[i]);
        }

        vector<double> result;
        for (auto query:queries) {
            if (vertices.count(query[0])&& vertices.count(query[1]) && find(vertices[query[0]])==find(vertices[query[1]])) {
                result.push_back(weight[vertices[query[0]]]/weight[vertices[query[1]]]);
            } else result.push_back(-1.0);
        }
        return result;
    }

    vector<double> bfs(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        unordered_map<string, int> vertices;
        int ver_count = 0;
        for (int i=0; i<equations.size(); i++) {
            for (int j=0; j<equations[i].size(); j++) {
                if (vertices.find(equations[i][j]) == vertices.end()) vertices[equations[i][j]] = ver_count++;
            }
        }

        vector<vector<pair<int, double>>> ajacent_lists(ver_count);
        for (int i=0; i<equations.size(); i++) {
            int v_from = vertices[equations[i][0]], v_to = vertices[equations[i][1]];
            ajacent_lists[v_from].push_back(make_pair(v_to, values[i]));
            ajacent_lists[v_to].push_back(make_pair(v_from, 1.0 / values[i]));
        }

        vector<double> result;
        for (int i=0; i<queries.size(); i++) {
            double res = -1.0;
            if (vertices.find(queries[i][0]) != vertices.end() && vertices.find(queries[i][1]) != vertices.end()) {
                int v_from = vertices[queries[i][0]], v_to = vertices[queries[i][1]];
                if (v_from == v_to) res = 1.0;
                else {
                    queue<int> reached;
                    reached.push(v_from);
                    vector<double> cost(ver_count, -1.0);
                    cost[v_from] = 1.0;
                    while (!reached.empty() && cost[v_to] < 0) {
                        int v_cur = reached.front();
                        reached.pop();

                        for (const auto [u, u_cost] : ajacent_lists[v_cur]) {
                            if (cost[u] < 0) {
                                cost[u] = cost[v_cur] * u_cost;
                                reached.push(u);
                            }
                        }
                    }
                    res = cost[v_to];
                }
            }
            result.push_back(res);
        }
        return result;
    }

public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        return union_find(equations, values, queries);
    }
};
// @lc code=end

