class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        from collections import Counter
        s_c = Counter(secret)
        g_c = Counter(guess)
        t = sum(i == j for i, j in zip(secret, guess))
        return "{}A{}B".format(t, sum((s_c & g_c).values()) - t)

secret = '1122'
guess  = '1222'
print(Solution().getHint(secret,guess))