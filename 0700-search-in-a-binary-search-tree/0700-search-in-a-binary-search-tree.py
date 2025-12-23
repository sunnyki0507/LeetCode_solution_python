# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        if not root:
            return None
        self.found = 0
        self.result = None

        def find(node, value):
            if node.val == value:
                self.result = node
                self.found = 1
                return node
            else:
                if node.left:
                    find(node.left, value)
                if node.right:
                    find(node.right, value)
        
        # node = find(root, val)
        find(root, val)
        print(self.found)
        return self.result
            
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        