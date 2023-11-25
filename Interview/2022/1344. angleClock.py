class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        a = abs((hour * 30 + minutes / 2 - minutes * 6))
        return a if a <= 180 else 360-a

hour = 12
minutes = 30
print(Solution().angleClock(hour,minutes))