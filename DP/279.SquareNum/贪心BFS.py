class Solution:
    def numSquares(self, n: int) -> int:
        squarenum = [(i + 1) ** 2 for i in range(round(n ** 0.5))]
        queue = {n}
        level = 0
        while queue:
            level += 1
            new_queue = set()
            for remnant in queue:
                for num in squarenum:
                    if remnant == num:
                        return level
                    elif remnant > num:
                        new_queue.add(remnant - num)
                    else:
                        break
            queue = new_queue
        return level


print(Solution().numSquares(365472456))