class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
    def treeToDoublyList(self, root: TreeNode) -> Node:
        nums = []
        self.traverseBST(root, nums)
        head = Node(nums[0],None,None)
        prev = head

        for i in range(1, len(nums)):
            cur = Node(nums[i], prev, None)
            prev.right = cur
            prev = cur
        cur.right = head
        head.left = cur
        return head


    def traverseBST(self, root:TreeNode, nums:list):
        if not root:
            return
        self.traverseBST(root.left, nums)
        nums.append(root.val)
        self.traverseBST(root.right,nums)
        return

nums = [2,1,3]
nums.sort()
BST = array_to_bst(nums)
ll = Solution().treeToDoublyList(BST)
s = ll
ll = ll.right
while s != ll:
    print(ll.val,ll.left.val)
    ll = ll.right