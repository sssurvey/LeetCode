# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# problem 112


#      5
#     / \
#    4   8
#   /   / \
#  11  13  4
# /  \      \
#7    2      1

# argument root = tree, sum = sum
# return = boolean
# True if there is a path added up to the sum, then return True

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.helper(root, 0, sum)

    def helper(self, root, path, sum):
        if root == None:                                 return False
        if root.left == None and root.right == None:
            if path + root.val == sum:                   return True
            else:                                        return False
        else:
            return self.helper(root.left, path + root.val, sum) \
            or self.helper(root.right, path + root.val, sum)
