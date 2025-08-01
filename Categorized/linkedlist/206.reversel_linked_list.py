# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        cur = head

        while cur:
            after = cur.next
            cur.next = prev
            prev = cur
            cur = after

        return prev


def toLinkedList(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head

    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def toList(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next

    return result


# Recursion
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head:
#             return None

#         newHead = head
#         if head.next:
#             newHead = self.reverseList(head.next)
#             head.next.next = head
#         head.next = None

#         return newHead


l1 = toLinkedList([1, 2, 3, 4, 5])
s = Solution()
x = s.reverseList(l1)
print(toList(x))
