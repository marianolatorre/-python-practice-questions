# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.compare(root, root)
    def compare(self, t1: TreeNode, t2: TreeNode) -> bool:
        
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None: 
            return False
        # print(t1,t2)/
        return t1.val == t2.val and \
                self.compare(t1.left, t2.right) and \
                self.compare(t2.left, t1.right)
