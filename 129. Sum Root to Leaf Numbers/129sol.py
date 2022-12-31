# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def addNum(num, val):
            return num*10 + val
        
        def recursive(num : int, node : Optional[TreeNode]):
            num = addNum(num, node.val)
            _sum = 0
            isLeaf = True
            if node.left:
                isLeaf = False
                _sum += recursive(num, node.left)
            if node.right:
                isLeaf = False
                _sum += recursive(num, node.right)
            if isLeaf:
                _sum = num
            return _sum
        
        return recursive(0, root)