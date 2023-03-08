class Solution:
    def maximumTime(self, time: str) -> str:
        if time[0] == '?':
            if time[1] == '?' or int(time[1]) < 4:
                time += '2'
            else:
                time += '1'
        else:
            time += time[0]
        if time[1] == '?':
            if time[5] == '2':
                time += '3'
            else:
                time += '9'
        else:
            time += time[1]
        time += ':'
        if time[3] == '?':
            time += '5'
        else:
            time += time[3]
        if time[4] == '?':
            time += '9'
        else:
            time += time[4]
        return time[5:]


time = "??:22"
print(Solution().maximumTime(time))