'''
左子树和右子树的最大深度又可以以同样的方式进行计算。
因此我们可以用「深度优先搜索」的方法来计算二叉树的最大深度。
具体而言，在计算当前二叉树的最大深度时，可以先递归计算出其左子树和右子树的最大深度，
然后在 O(1) 时间内计算出当前二叉树的最大深度。递归在访问到空节点时退出。

'''


class Solution:
    def maxDepth(self, root):
        if root is None: 
            return 0 
        else: 
            left_height = self.maxDepth(root.left) 
            right_height = self.maxDepth(root.right) 
            return max(left_height, right_height) + 1 
