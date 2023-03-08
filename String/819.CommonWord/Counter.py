class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        import collections
        banset = set(banned)
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        count = collections.Counter(
            word for word in paragraph.lower().split())
        ans, best = '', 0
        for word in count:
            if count[word] > best and word not in banset:
                ans, best = word, count[word]

        return ans

case = Solution()
print(case.mostCommonWord('Bob hit a ball; the hit BALL flew far after it was hit!', {'hit'}))
