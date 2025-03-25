from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 方法一：将值复制到数组中后用双指针法
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        cur_head = head
        while cur_head:
            vals.append(cur_head.val)
            cur_head = cur_head.next
        
        return vals == vals[::-1]
    

# test
def test():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    s = Solution()
    res = s.isPalindrome(head)
    print(res)
    
test()

