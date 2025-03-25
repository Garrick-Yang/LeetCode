# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        res = l1
        pre = None
        add_item_10 = 0
        while l1 and l2:
            add_item = l1.val + l2.val + add_item_10
            add_item_re = add_item % 10
            add_item_10 = add_item // 10

            l1.val = add_item_re
            pre = l1
            l1 = l1.next
            l2 = l2.next

        while l1 is not None or l2 is not None:
            if l1 is None and l2 is not None:
                add_item = l2.val + add_item_10
                add_item_re = add_item % 10
                add_item_10 = add_item // 10
                l2.val = add_item_re
                pre.next = l2
                pre = l2
                l2 = l2.next
            
            if l2 is None and l1 is not None:
                add_item = l1.val + add_item_10
                add_item_re = add_item % 10
                add_item_10 = add_item // 10
                l1.val = add_item_re
                pre.next = l1
                pre = l1
                l1 = l1.next

            if add_item_10 != 0 and l1 is None and l2 is None:
                new_head = ListNode()
                new_head.val = add_item_10
                add_item_10 = 0
                pre.next = new_head
        
        if add_item_10 != 0 and l1 is None and l2 is None:
            new_head = ListNode()
            new_head.val = add_item_10
            add_item_10 = 0
            pre.next = new_head

        return res


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head, tail = None, None
        carry = 0
        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            sum = n1 + n2 + carry
            carry = sum // 10
            if not head:
                head = tail = ListNode(sum % 10)
            else:
                tail.next = ListNode(sum % 10)
                tail = tail.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:
            tail.next = ListNode(carry)
        return head



# test
l1 = ListNode(2, ListNode(4, ListNode(9)))
l2 = ListNode(5, ListNode(6, ListNode(4, ListNode(9))))
s = Solution().addTwoNumbers(l1, l2)
while s:
    print(s.val)
    s = s.next
# Output: 7 -> 0 -> 8
