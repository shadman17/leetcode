# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         nodes = []

#         for lst in lists:
#             while lst:
#                 nodes.append(lst.val)
#                 lst = lst.next

#         nodes.sort()

#         dummy = ListNode()
#         temp = dummy

#         for node in nodes:
#             temp.next = ListNode(node)
#             temp = temp.next

#         return dummy.next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2list(head1, head2):
            dummy = ListNode(-1)
            temp = dummy

            while head1 and head2:
                if head1.val < head2.val:
                    temp.next = head1
                    head1 = head1.next

                else:
                    temp.next = head2
                    head2 = head2.next

                temp = temp.next

            temp.next = head1 if head1 else head2

            return dummy.next

        def merge(head, lists):
            for i in range(1, len(lists)):
                head = merge2list(head, lists[i])
            return head


        if len(lists) == 0:
            return None
        return merge(lists[0], lists)


# import heapq
# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         min_heap = []

#         for i in range(len(lists)):
#             if lists[i] is not None:
#                 heapq.heappush(min_heap, (lists[i].val, i, lists[i]))
        

#         dummy = ListNode(-1)
#         tail = dummy

#         while min_heap:
#             val, i, node = heapq.heappop(min_heap)
#             tail.next = node
#             tail = tail.next

#             if node.next:
#                 heapq.heappush(min_heap, (node.next.val, i, node.next))

#         return dummy.next