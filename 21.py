from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
递归
如果 l1 或者 l2 一开始就是空链表 ，那么没有任何操作需要合并，所以我们只需要返回非空链表。
否则，我们要判断 l1 和 l2 哪一个链表的头节点的值更小，然后递归地决定下一个添加到结果里的节点。
如果两个链表有一个为空，递归结束。
'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1=list1.next, list2=list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1=list1, list2=list2.next)
            return list2


'''
我们可以用迭代的方法来实现上述算法。
当 l1 和 l2 都不是空链表时，判断 l1 和 l2 哪一个链表的头节点的值更小，
将较小值的节点添加到结果里，当一个节点被添加到结果里之后，
将对应链表中的节点向后移一位。

'''
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        pre = head

        while l1 and l2:
            if l1.val < l2.val:
                pre.next = l1
                l1 = l1.next

            else:
                pre.next = l2
                l2 = l2.next

            pre = pre.next

        pre.next = l1 if l2 is None else l2

        return head.next