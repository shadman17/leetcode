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
        if len(lists) == 0:
            return None

        for i in range(1, len(lists)):
            lists[i] = self.mergeList(lists[i - 1], lists[i])

        return lists[-1]

    def mergeList(self, list1, list2):
        dummy = ListNode()
        temp = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next

            temp = temp.next

        temp.next = list1 if list1 else list2

        return dummy.next


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