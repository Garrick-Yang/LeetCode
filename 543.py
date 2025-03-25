# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        self.ans = 0
        def depth(node):
            if node is None:
                return 0
            
            l = depth(node.left)
            r = depth(node.right)
            self.ans = max(self.ans, l + r)
            return max(l, r) + 1
        
        depth(root)
        return self.ans


class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        self.ans = 0
        def depth(node):
            # 访问到空节点了，返回0
            if not node:
                return 0
            # 左儿子为根的子树的深度
            L = depth(node.left)
            # 右儿子为根的子树的深度
            R = depth(node.right)
            # 计算d_node即L+R+1 并更新ans
            self.ans = max(self.ans, L + R)
            # 返回该节点为根的子树的深度
            return max(L, R) + 1

        depth(root)
        return self.ans

        