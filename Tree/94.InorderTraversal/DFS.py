class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def arr2tree(self, nums: list) -> TreeNode:
        def level(index):
            if index > len(nums) or nums[index] == None:
                return None
            root = TreeNode(nums[index], None, None)
            root.left = level(index * 2 + 1)
            root.right = level(index * 2 + 2)
            return root
        root = level(0)
        return root

    def inorderTraversal(self, root: TreeNode) -> list:
        ans = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)
        dfs(root)
        return ans


root = [1, None, 2,None,None, 3,None]
Root = Solution().arr2tree(root)
print(Solution().inorderTraversal(Root))