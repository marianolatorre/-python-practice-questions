# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def comp(self, root: TreeNode, comparable)-> int:
        result = root.val
        if root.left is not None:
            result = comparable(self.comp(root.left, comparable),result)
        if root.right is not None:
            result = comparable(self.comp(root.right, comparable),result)
        return result
            
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        if root.left is not None and root.val <= self.comp(root.left,max): 
            return False
        elif root.right is not None and root.val >= self.comp(root.right,min):
            return False
        
        return self.isValidBST(root.left ) and self.isValidBST(root.right)