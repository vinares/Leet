#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
from telnetlib import WONT


class TrieNode:
    def __init__(self, words=0, is_word=False, nexts=dict()) -> None:
        self.words = words
        self.is_word = is_word
        self.next = nexts

class Trie:
    def __init__(self):
        self.root = TrieNode(0, False, dict())

    def insert(self, word: str) -> None:
        root = self.root
        for c in word:
            if c not in root.next:
                root.next[c] = TrieNode(0, False, dict())
            root.words += 1
            root = root.next[c]
        root.is_word = True
        root.words += 1

    def search(self, word: str) -> bool:
        root = self.root
        for c in word:
            if c not in root.next:
                return False
            root = root.next[c]
        return root.is_word

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for c in prefix:
            if c not in root.next:
                return False
            root = root.next[c]
        return root.words > 0


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

