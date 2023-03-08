--
-- @lc app=leetcode id=511 lang=mysql
--
-- [511] Game Play Analysis I
--

-- @lc code=start
# Write your MySQL query statement below
SELECT 
    player_id,
    min(event_date) first_login
FROM Activity
GROUP BY player_id

-- @lc code=end

