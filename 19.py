# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

''''
在对链表进行操作时，一种常用的技巧是添加一个哑节点（dummy node），它的 next 指针指向链表的头节点。这样一来，我们就不需要对头节点进行特殊的判断了。

首先从头节点开始对链表进行一次遍历，得到链表的长度 L。
随后我们再从头节点开始对链表进行一次遍历，当遍历到第 L−n+1 个节点时，它就是我们需要删除的节点。
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.get_length(head=head)
        num = length - n + 1
        pre = ListNode(next=head)
        temp = pre
        i = 0
        while temp:
            if i == num - 1:
                temp.next = temp.next.next
            i = i + 1
            temp = temp.next

        return pre.next

    def get_length(self, head):
        length = 0
        while head:
            length = length + 1
            head = head.next
        return length

'''
根据栈「先进后出」的原则，我们弹出栈的第 n 个节点就是需要删除的节点，并且目前栈顶的节点就是待删除节点的前驱节点。
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = list()
        pre = ListNode(next=head)
        cur = pre 
        while cur:
            stack.append(cur)
            cur = cur.next
        
        for i in range(n):
            stack.pop()
        
        temp = stack[-1]
        temp.next = temp.next.next

        return pre.next
    
'''
可以使用两个指针 first 和 second 同时对链表进行遍历，并且 first 比 second 超前 n 个节点。
当 first 遍历到链表的末尾时，second 就恰好处于倒数第 n 个节点。
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pre = ListNode(next=head)
        fast, slow = pre, pre
        for i in range(n + 1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return pre.next


# test 
l1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5)))))
s = Solution()
s.removeNthFromEnd(head=l1, n=2)
while l1:
    print(l1.val)
    l1 = l1.next
