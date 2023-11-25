class Solution:
    def exclusiveTime(self, n: int, logs: list) -> list:
        stack = []
        ans = [0] * n

        for i, l in enumerate(logs):
            ll = l.split(':')
            id, Type, stamp = int(ll[0]), ll[1], int(ll[2])

            if Type == 'start':
                if stack:
                    old_stamp = stack.pop()
                    old_id = stack.pop()
                    ans[old_id] += stamp - old_stamp
                    stack.append(old_id)
                stack.append(id)
                stack.append(stamp)
            else:
                stamp += 1
                old_stamp = stack.pop()
                old_id = stack.pop()
                ans[old_id] += stamp - old_stamp
                if stack: stack.append(stamp)
        return ans



n = 3
logs = ["0:start:0","0:end:0","1:start:1","1:end:1","2:start:2","2:end:2","2:start:3","2:end:3"]
print(Solution().exclusiveTime(n, logs))