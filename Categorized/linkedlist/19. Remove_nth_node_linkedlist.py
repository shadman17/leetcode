# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head

        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return head


def list_to_linkedlist(values):
    """Convert a list to a linked list."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linkedlist_to_list(head):
    """Convert a linked list back to a list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def test():
    sol = Solution()

    # Test Case 1
    head = list_to_linkedlist([1, 2, 3, 4, 5])
    n = 2
    new_head = sol.removeNthFromEnd(head, n)
    assert linkedlist_to_list(new_head) == [1, 2, 3, 5]

    # Test Case 2: Remove last element
    head = list_to_linkedlist([1, 2])
    n = 1
    new_head = sol.removeNthFromEnd(head, n)
    assert linkedlist_to_list(new_head) == [1]

    # Test Case 3: Remove first element
    head = list_to_linkedlist([1])
    n = 1
    new_head = sol.removeNthFromEnd(head, n)
    assert linkedlist_to_list(new_head) == []

    print("All test cases passed!")


test()
