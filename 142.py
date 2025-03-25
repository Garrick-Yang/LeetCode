from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
方法一：哈希表
一个非常直观的思路是：我们遍历链表中的每个节点，并将它记录下来；一旦遇到了此前遍历过的节点，就可以判定链表中存在环。借助哈希表可以很方便地实现。
'''
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        current = head

        while current:
            if current in visited:
                return current
            
            visited.add(current)
            current = current.next

        return None
    
'''
方法二：快慢指针（Floyd 判圈算法）
该方法使用两个指针，一个慢指针（每次移动一步）和一个快指针（每次移动两步）。
如果链表中存在环，两个指针最终会在环中相遇。
当找到相遇点后，将其中一个指针重新指向头节点，然后两个指针以相同的速度移动，
它们会在环的入口处相遇。

由于 fast 指针每次移动两步，slow 指针每次移动一步，所以 fast 指针相对于 slow 指针每次移动一步（2 - 1 = 1）。也就是说，每经过一个单位时间，fast 指针和 slow 指针之间的相对距离就会减少 1。
所以在slow第一圈的时候一定会相遇
'''
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                ptr = head
                while ptr != slow:
                    ptr = ptr.next
                    slow = slow.next

                return ptr
        return None