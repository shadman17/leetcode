from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next

            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next
    
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy

    for value in lst:
        current.next = ListNode(value)
        current = current.next

    return dummy.next

def print_linked_list(node):
    values = []

    while node:
        values.append(node.val)
        node = node.next

    print(values)

list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])
solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)
print_linked_list(merged_list)