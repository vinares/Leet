/*
 * @lc app=leetcode id=721 lang=cpp
 *
 * [721] Accounts Merge
 */

// @lc code=start
class Solution {
   public:
    unordered_map<string, int> email_to_index;
    int* uf;
    int f(int i) { return uf[i] == i ? i : uf[i] = f(uf[i]); }
    void u(int i, int j) { uf[f(i)] = f(j); }

    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        int n = accounts.size();
        uf = new int[n];
        for (int i = 0; i < n; i++) {
            uf[i] = i;
            for (int j = 1; j < accounts[i].size(); j++) {
                string& email = accounts[i][j];
                if (email_to_index.count(email))
                    u(email_to_index[email], i);
                else
                    email_to_index[email] = i;
            }
        }

        unordered_map<int, vector<string>> index_to_emails;
        for (auto& email_index_pair : email_to_index) {
            index_to_emails[f(email_index_pair.second)].push_back(
                move(email_index_pair.first));
        }

        vector<vector<string>> result;
        for (auto& index_emails_pair : index_to_emails) {
            result.push_back({});
            result.back().push_back(move(accounts[index_emails_pair.first][0]));
            result.back().insert(result.back().end(),
                                 index_emails_pair.second.begin(),
                                 index_emails_pair.second.end());
            sort(result.back().begin() + 1, result.back().end());
        }
        delete[] uf;
        return result;
    }
};
// @lc code=end
