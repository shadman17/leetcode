# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         seen = set()

#         cur = head
#         while cur:
#             if cur in seen:
#                 return cur
#             seen.add(cur)
#             cur = cur.next

#         return None
    

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        if not fast or not fast.next:
            return None
        
        slow2 = head

        while slow != slow2:
            slow = slow.next
            slow2 = slow2.next

        return slow
        


def build_linked_list_with_cycle(values, pos):
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    nodes = [head]

    for val in values[1:]:
        new_node = ListNode(val)
        current.next = new_node
        current = new_node
        nodes.append(new_node)
    
    if pos != -1:
        # Create the cycle
        current.next = nodes[pos]

    return head

# Test data
values = [3, 2, 0, -4]
pos = 1

# Build the linked list
head = build_linked_list_with_cycle(values, pos)

# Create an instance of Solution and test
sol = Solution()
cycle_node = sol.detectCycle(head)

# # Print the value of the node where the cycle starts
# if cycle_node:
#     print("Cycle starts at node with value:", cycle_node.val)
# else:
#     print("No cycle detected.")
