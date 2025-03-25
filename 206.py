# import Optional
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 迭代
class Solution_1:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre  
            pre = cur
            cur = tmp
        return pre

# 循环
class Solution_2:
    def reverseList(self, head):
        ans = None
        x = head
        while x is not None:
            ans = ListNode(x.val, ans)
            x = x.next
        return ans

# 递归
class Solution:
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
            
# test
def test():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    s = Solution()
    new_head = s.reverseList(head)
    while new_head:
        print(new_head.val)
        new_head = new_head.next

test()
