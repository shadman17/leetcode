# Definition for singly-linked list.
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)

        prev1 = dummy1
        prev2 = dummy2
        current = head

        while current:
            if current.val < x:
                prev1.next = current
                prev1 = current
            else:
                prev2.next = current
                prev2 = current

            current = current.next

        prev2.next = None
        prev1.next = dummy2.next

        return dummy1.next


def list_to_linkedlist(values):
    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linkedlist_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next

    return result


s = Solution()
ll = list_to_linkedlist([1, 4, 3, 2, 5, 2])
ll1 = s.partition(ll, 3)
print(linkedlist_to_list(ll1))
