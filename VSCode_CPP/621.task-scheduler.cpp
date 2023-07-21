/*
 * @lc app=leetcode id=621 lang=cpp
 *
 * [621] Task Scheduler
 */

// @lc code=start
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        int time_stamp = 0;
        unordered_map<char, int> task_counter;
        
        for (auto task : tasks) {
            task_counter[task]++;
        }

        int max_exec = max_element(task_counter.begin(), task_counter.end(), [](const auto &u, const auto &v) -> bool {
            return u.second < v.second;
        })->second;

        int max_exec_elements = accumulate(task_counter.begin(), task_counter.end(), 0, [=](int acc, const auto &u){
            return acc + (u.second == max_exec);
        });
        return max((max_exec-1) * (n+1) + max_exec_elements, static_cast<int>(tasks.size()));

    }
};
// @lc code=end
