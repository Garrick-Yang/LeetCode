# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




'''
错误解法
无法判断右边子树的某个节点比root或者左边值小的情况
'''
class Solution:
    def isValidBST(self, root):
        def helper(root):
            if root.left is None and root.right is None:
                return True
            
            if root.left is None and root.right is not None:
                lower = float('-inf')
                upper = root.right.val
            if root.left is not None and root.right is None:
                lower = root.left.val
                upper = float('inf')
            if root.left is not None and root.right is not None:
                lower = root.left.val
                upper = root.right.val

            val = root.val
            if val <= lower or val >= upper:
                return False
            
            if root.left is not None and not helper(root.left):
                return False
            
            if root.right is not None and not helper(root.right):
                return False
            
            return True
        
        return helper(root)
'''
如果该二叉树的左子树不为空，则左子树上所有节点的值均小于它的根节点的值； 
若它的右子树不空，则右子树上所有节点的值均大于它的根节点的值；
它的左右子树也为二叉搜索树。

'''
class Solution:
    def isValidBST(self, root):
        def helper(root, lower = float('-inf'), upper = float('inf')):
            if not root:
                return True
            
            val = root.val
            if val <= lower or val >= upper:
                return False
            if not helper(root.left, lower, val):
                return False
            if not helper(root.right, val, upper):
                return False
            return True
        return helper(root)


'''
二叉搜索树「中序遍历」得到的值构成的序列一定是升序的，
这启示我们在中序遍历的时候实时检查当前节点的值是否大于前一个中序遍历到的节点的值即可。
如果均大于说明这个序列是升序的，整棵树是二叉搜索树，否则不是
'''
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, inorder = [], float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True

