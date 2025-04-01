class Solution:
    def kthSmallest(self, root, k):
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

'''
深度优先遍历
'''

class Solution:
    def kthSmallest(self, root, k: int) -> int:
        # 定义一个内部的深度优先搜索（DFS）函数，用于进行中序遍历
        def dfs(node)->int:
            # 如果当前节点为空，返回 -1 表示未找到目标节点
            if node is None:
                return -1
            
            # 递归调用 dfs 函数处理左子树
            left_res = dfs(node.left)
            # 如果在左子树中找到了第 k 小的元素，直接返回该元素的值
            if left_res != -1:
                return left_res

            # 使用 nonlocal 关键字声明 k 是外部函数的变量，对其进行减 1 操作
            nonlocal k 
            k -= 1
            # 当 k 减到 0 时，说明当前节点就是第 k 小的元素，返回该节点的值
            if k == 0:
                return  node.val

            # 如果还未找到第 k 小的元素，递归调用 dfs 函数处理右子树
            return dfs(node.right)
            
        # 调用 dfs 函数从根节点开始进行中序遍历，并返回结果
        return dfs(root)
