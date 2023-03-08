#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()
        q = deque([0])

        while q:
            cur = q.popleft()
            visited.add(cur)
            for node in rooms[cur]:
                if node not in visited:
                    q.append(node)
        return len(visited) == n


# @lc code=end

