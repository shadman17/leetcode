# class Node:
#     def __init__(self, url: str):
#         self.url = url
#         self.prev = None
#         self.next = None


# class BrowserHistory:

#     def __init__(self, homepage: str):
#         self.head = Node(homepage)

#     def visit(self, url: str) -> None:
#         new_node = Node(url)
#         self.head.next = new_node
#         new_node.prev = self.head
#         self.head = new_node

#     def back(self, steps: int) -> str:
#         while steps > 0 and self.head.prev:
#             self.head = self.head.prev
#             steps -= 1
#         return self.head.url

#     def forward(self, steps: int) -> str:
#         while steps > 0 and self.head.next:
#             self.head = self.head.next
#             steps -= 1
#         return self.head.url


class ListNode:
    def __init__(self, data="", prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.currentnode = ListNode(homepage)


    def visit(self, url: str) -> None:
        newnode = ListNode(url)
        self.currentnode.next = newnode
        newnode.prev = self.currentnode
        self.currentnode = newnode

    def back(self, steps: int) -> str:
        while self.currentnode.prev is not None and steps > 0:
            steps -= 1
            self.currentnode = self.currentnode.prev

        return self.currentnode.data


    def forward(self, steps: int) -> str:
        while self.currentnode.next is not None and steps > 0:
            steps -= 1
            self.currentnode = self.currentnode.next

        return self.currentnode.data



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
