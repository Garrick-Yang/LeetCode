
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
选择中间位置左边的数字作为根节点，则根节点的下标为 mid=(left+right)/2，此处的除法为整数除法
'''
class Solution:
    def sortedArrayToBST(self, nums):
        def helper(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = helper(left, mid - 1)
            node.right = helper(mid + 1, right)

            return node
        
        return helper(0, len(nums) - 1)