# Definition for singly-linked list.
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101)
        prev = dummy
        current = head
        while current:
            if current.val == prev.val:
                current = current.next

            else:
                prev.next = current
                current = current.next
                prev = prev.next

        prev.next = None

        return dummy.next


def list_to_ll(values):
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def ll_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next

    return result


s = Solution()
linkedlist = list_to_ll([1, 2, 3, 3])
result = s.deleteDuplicates(linkedlist)
print(ll_to_list(result))
