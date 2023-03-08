#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#

# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            done = True
            while done and ast < 0  and stack and stack[-1] > 0:
                done = -ast > stack[-1]
                if stack[-1] <= -ast:
                    stack.pop()
            if done:
                stack.append(ast)
        return stack



# @lc code=end

