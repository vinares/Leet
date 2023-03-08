class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        Bulls, Cows = 0, 0
        secret_Hash = dict()

        for x in secret:
            if x not in secret_Hash:
                secret_Hash[x] = 1
            else:
                secret_Hash[x] += 1
        for i, x in enumerate(guess):
            if x == secret[i]:
                Bulls += 1
                secret_Hash[x] -= 1

        for i, x in enumerate(guess):
            if x != secret[i] and x in secret_Hash and secret_Hash[x]:
                Cows += 1
                secret_Hash[x] -= 1
        return str(Bulls) + 'A' + str(Cows) + 'B'

secret = '1122'
guess  = '1222'
print(Solution().getHint(secret,guess))