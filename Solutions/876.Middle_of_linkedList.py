# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        a = head
        b = head

        count = 0
        mid = 0
        while a.next:
            a = a.next
            count += 1

        if count % 2 == 1:
            mid = count // 2
        else:
            mid = count // 2 + 1

        for _ in range(mid):
            b = b.next

        return b


def create_linked_list(lst):
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


lst = [1, 2, 3, 4, 5]
head = create_linked_list(lst)
solution = Solution()
middle_node = solution.middleNode(head)

# Print the middle node and the rest of the linked list
print_linked_list(middle_node)
