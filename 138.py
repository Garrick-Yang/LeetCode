# Definition for a Node.
from typing import Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

'''
本题要求我们对一个特殊的链表进行深拷贝。
如果是普通链表，我们可以直接按照遍历的顺序创建链表节点。
而本题中因为随机指针的存在，当我们拷贝节点时，「当前节点的随机指针指向的节点」可能还没创建，
因此我们需要变换思路。一个可行方案是，我们利用回溯的方式，让每个节点的拷贝操作相互独立。
对于当前节点，我们首先要进行拷贝，然后我们进行「当前节点的后继节点」和「当前节点的随机指针指向的节点」拷贝，
拷贝完成后将创建的新节点的指针返回，即可完成当前节点的两指针的赋值。

具体地，我们用哈希表记录每一个节点对应新节点的创建情况。
遍历该链表的过程中，我们检查「当前节点的后继节点」和「当前节点的随机指针指向的节点」的创建情况。
如果这两个节点中的任何一个节点的新节点没有被创建，我们都立刻递归地进行创建。
当我们拷贝完成，回溯到当前层时，我们即可完成当前节点的指针赋值。
注意一个节点可能被多个其他节点指向，因此我们可能递归地多次尝试拷贝某个节点，为了防止重复拷贝，
我们需要首先检查当前节点是否被拷贝过，如果已经拷贝过，我们可以直接从哈希表中取出拷贝后的节点的指针并返回即可。

'''

class Solution:
    def __init__(self):
        # 用于缓存已经复制过的节点
        self.cachedNode = {}
    def copyRandomList(self, head: 'Node') -> 'Node':
        # 如果头节点为空，直接返回 None
        if not head:
            return None
        # 如果该节点还未被复制
        if head not in self.cachedNode:
            # 创建新节点
            headNew = Node(head.val)
            # 将原节点和新节点的映射存入缓存
            self.cachedNode[head] = headNew
            # 递归复制下一个节点
            headNew.next = self.copyRandomList(head.next)
            # 递归复制随机指针指向的节点
            headNew.random = self.copyRandomList(head.random)
        # 返回缓存中该节点对应的新节点
        return self.cachedNode[head]


'''
我们首先将该链表中每一个节点拆分为两个相连的节点，
例如对于链表 A→B→C，我们可以将其拆分为 A→A′→B→B′→C→C′。
对于任意一个原节点 S，其拷贝节点 S′即为其后继节点。

这样，我们可以直接找到每一个拷贝节点 S ′的随机指针应当指向的节点，
即为其原节点 S 的随机指针指向的节点 T 的后继节点 T ′。
需要注意原节点的随机指针可能为空，我们需要特别判断这种情况。

'''
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        # 第一步，复制每个节点，并将复制的节点插入到对应的原节点后面
        cur = head
        while cur:
            curCopy = Node(cur.val)
            curCopy.next = cur.next
            cur.next = curCopy
            cur = curCopy.next
        # 第二步，设置复制节点的随机指针
        cur = head
        while cur:
            curCopy = cur.next
            if cur.random:
                curCopy.random = cur.random.next
            cur = curCopy.next
        # 第三步，拆分两个链表
        cur = head
        headCopy = head.next
        while cur.next:
            curCopy = cur.next
            cur.next = curCopy.next
            cur = curCopy
        return headCopy


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # 如果头节点为空，直接返回 None
        if head is None:
            return None
        # 用于存储原节点到新节点的映射
        node_map = {}
        # 第一次遍历链表，创建新节点并建立映射
        current = head
        while current:
            node_map[current] = Node(current.val)
            current = current.next

        # 第二次遍历链表，设置新节点的 next 和 random 指针
        current = head
        while current:
            new_node = node_map[current]
            # 设置新节点的 next 指针
            new_node.next = node_map.get(current.next)
            # 设置新节点的 random 指针
            new_node.random = node_map.get(current.random)
            current = current.next

        # 返回新链表的头节点
        return node_map[head]
