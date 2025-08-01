class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1

        cnt = 0
        temp = self.head.next

        while temp:
            if cnt == index:
                return temp.val
            temp = temp.next
            cnt += 1

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        temp = self.head
        for _ in range(self.size):
            temp = temp.next

        temp.next = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        node = ListNode(val)
        temp = self.head
        for _ in range(index):
            temp = temp.next

        node.next = temp.next
        temp.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        temp = self.head
        for _ in range(index):
            temp = temp.next

        temp.next = temp.next.next
        self.size -= 1


# self.head is None:

# class Node(object):

#     def __init__(self, val):
#         self.val = val
#         self.next = None


# class MyLinkedList(object):

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.head = None
#         self.size = 0

#     def get(self, index):
#         """
#         Get the value of the index-th node in the linked list. If the index is invalid, return -1.
#         :type index: int
#         :rtype: int
#         """
#         if index < 0 or index >= self.size:
#             return -1

#         if self.head is None:
#             return -1

#         curr = self.head
#         for i in range(index):
#             curr = curr.next
#         return curr.val

#     def addAtHead(self, val):
#         """
#         Add a node of value val before the first element of the linked list.
#         After the insertion, the new node will be the first node of the linked list.
#         :type val: int
#         :rtype: void
#         """
#         node = Node(val)
#         node.next = self.head
#         self.head = node

#         self.size += 1

#     def addAtTail(self, val):
#         """
#         Append a node of value val to the last element of the linked list.
#         :type val: int
#         :rtype: void
#         """
#         curr = self.head
#         if curr is None:
#             self.head = Node(val)
#         else:
#             while curr.next is not None:
#                 curr = curr.next
#             curr.next = Node(val)

#         self.size += 1

#     def addAtIndex(self, index, val):
#         """
#         Add a node of value val before the index-th node in the linked list.
#         If index equals to the length of linked list, the node will be appended to the end of linked list.
#         If index is greater than the length, the node will not be inserted.
#         :type index: int
#         :type val: int
#         :rtype: void
#         """
#         if index < 0 or index > self.size:
#             return

#         if index == 0:
#             self.addAtHead(val)
#         else:
#             curr = self.head
#             for i in range(index - 1):
#                 curr = curr.next
#             node = Node(val)
#             node.next = curr.next
#             curr.next = node

#             self.size += 1

#     def deleteAtIndex(self, index):
#         """
#         Delete the index-th node in the linked list, if the index is valid.
#         :type index: int
#         :rtype: void
#         """
#         if index < 0 or index >= self.size:
#             return

#         curr = self.head
#         if index == 0:
#             self.head = curr.next
#         else:
#             for i in range(index - 1):
#                 curr = curr.next
#             curr.next = curr.next.next

#         self.size -= 1
