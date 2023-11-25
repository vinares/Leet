class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        def check(s, t):
            for i, j in zip(s, t):
                if order.find(i) < order.find(j):
                    return True
                elif order.find(i) == order.find(j):
                    continue
                else:
                    return False

            if len(s) > len(t): return False
            return True

        for i in range(len(words) - 1):
            if not check(words[i], words[i + 1]): return False
        return True
