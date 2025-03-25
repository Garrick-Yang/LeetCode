import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None 
        self.right = None 

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            res.append([node.val for node in queue])
            queue = [child for node in queue for child in (node.left, node.right) if child]
        return res
    
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        dequeue = collections.deque([root])
        res = []
        while dequeue:
            level = []
            for _ in range(len(dequeue)):
                node = dequeue.popleft()
                level.append(node.val)
                if node.left:
                    dequeue.append(node.left)
                if node.right:
                    dequeue.append(node.right)
            res.append(level)
        return res