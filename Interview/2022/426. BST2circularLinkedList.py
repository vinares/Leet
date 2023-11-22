class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def array_to_bst(array_nums):
    if not array_nums:
        return None
    mid_num = len(array_nums)//2
    node = TreeNode(array_nums[mid_num])
    node.left = array_to_bst(array_nums[:mid_num])
    node.right = array_to_bst(array_nums[mid_num+1:])
    return node

def preOrder(node):
    if not node:
        return
    print(node.val)
    preOrder(node.left)
    preOrder(node.right)

class Solution:
    def treeToDoublyList(self, root: TreeNode) -> TreeNode:
        if not root: return root

        def inOrder(root):
            if not root.left:
                left = root
            else:
                left, _ = inOrder(root.left)
                _.right = root
                root.left = _
            if not root.right:
                right = root
            else:
                _, right = inOrder(root.right)
                root.right = _
                _.left = root
            return left, right

        left, right = inOrder(root)
        left.left = right
        right.right = left
        return left



    def traverseBST(self, root:TreeNode, nums:list):
        if not root:
            return
        self.traverseBST(root.left, nums)
        nums.append(root.val)
        self.traverseBST(root.right,nums)
        return

nums = [i for i in range(1, 11)]

BST = array_to_bst(nums)
ll = Solution().treeToDoublyList(BST)
while 1:
    print(ll.val)
    ll = ll.right