class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 如果链表为空或只有一个节点，直接返回
        if not head or not head.next:
            return head
        
        # 使用快慢指针找到链表中点
        slow = head
        fast = head.next  # fast比slow多走一步，确保奇数长度时slow停在中间
        
        # 快指针走两步，慢指针走一步
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 将链表从中点断开成两部分
        # second_half指向后半部分
        second_half = slow.next
        slow.next = None  # 前半部分断开
        
        # 递归地对前后两半部分排序
        left = self.sortList(head)
        right = self.sortList(second_half)
        
        # 合并两个已排序的子链表
        return self.merge(left, right)
    
    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 创建哑节点作为合并后链表的起始点
        dummy = ListNode(0)
        current = dummy
        
        # 当两个子链表都有节点时，比较并合并
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        # 如果l1还有剩余节点，直接连接
        if l1:
            current.next = l1
        
        # 如果l2还有剩余节点，直接连接
        if l2:
            current.next = l2
        
        # 返回合并后的链表头节点
        return dummy.next

# 测试代码
def create_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_list(head):
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    print(" -> ".join(values))

# 测试用例
if __name__ == "__main__":
    arr = [4, 2, 1, 3]
    head = create_list(arr)
    print("原始链表：")
    print_list(head)
    
    solution = Solution()
    sorted_head = solution.sortList(head)
    print("排序后链表：")
    print_list(sorted_head)