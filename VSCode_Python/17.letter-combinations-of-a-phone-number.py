#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = "abc def ghi jkl mno pqrs tuv wxyz".split()
        mapping = {str(digit): letter for digit, letter in enumerate(letters, 2)}
        answers = []
        for digit in digits:
            answers = [f"{answer}{letter}" for answer in answers or [''] for letter in mapping[digit]]
        return answers
# @lc code=end

