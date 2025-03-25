# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
如果链表中至少有两个节点，则在两两交换链表中的节点之后，
原始链表的头节点变成新的链表的第二个节点，原始链表的第二个节点变成新的链表的头节点。
链表中的其余节点的两两交换可以递归地实现。
在对链表中的其余节点递归地两两交换之后，更新节点之间的指针关系，即可完成整个链表的两两交换。

'''
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        new_head = head.next
        head.next = self.swapPairs(new_head.next)
        new_head.next = head

        return new_head
    
'''
创建哑结点 dummyHead，令 dummyHead.next = head。
令 temp 表示当前到达的节点，初始时 temp = dummyHead。每次需要交换 temp 后面的两个节点。
'''

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = ListNode(next=head)
        temp = pre
        while temp.next and temp.next.next:
            node1 = temp.next
            node2 = temp.next.next
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            temp = temp.next.next
        return pre.next


# test
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
s = Solution()
res = s.swapPairs(head)
while res:
    print(res.val)
    res = res.next
