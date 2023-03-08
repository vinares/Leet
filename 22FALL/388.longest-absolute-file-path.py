#
# @lc app=leetcode id=388 lang=python3
#
# [388] Longest Absolute File Path
#

# @lc code=start
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        directory = []
        files_and_dirs = input.split('\n')
        longest = 0
        
        for i in range(len(files_and_dirs)):
            is_file = '.' in files_and_dirs[i]
            level = 0
            j = 0
            while j < len(files_and_dirs[i]):
                if files_and_dirs[i][j] == '\t':
                    j += 1
                    level += 1
                else:
                    break
            if is_file:
                file_name = []
                for dir_name, l in directory:
                    if l < level:
                        file_name.append(dir_name)
                    else:
                        break
                if len(file_name) >= 0:
                    file_name.append(files_and_dirs[i][j::])
                file = '/'.join(file_name)
                longest = max(longest, len(file))
            else:
                while directory and directory[-1][1] >= level:
                    directory.pop()
                directory.append((files_and_dirs[i][j::], level))
        return longest
# @lc code=end

