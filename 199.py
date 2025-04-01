'''
和层序遍历代码几乎相同，就是添加改为每行最后一个
'''

class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            res.append(queue[-1].val)
            queue = [child for node in queue for child in (node.left, node.right) if child]
        return res
    
class Solution:
    def rightSideView(self, root):
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
            res.append(level[-1])
        return res