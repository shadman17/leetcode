class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.next = self.head

    def removeNode(self, node):
        prevnode = node.prev
        afternode = node.next
        prevnode.next = afternode
        afternode.prev = prevnode

    def insertafterhead(self, node):
        currentnode = self.head.next
        self.head.next = node
        node.next = currentnode
        node.prev = self.head
        currentnode.prev = node

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        node = self.hashmap[key]
        self.removeNode(node)
        self.insertafterhead(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.removeNode(node)
            self.insertafterhead(node)
        else:
            if len(self.hashmap) == self.capacity:
                node = self.tail.prev
                del self.hashmap[node.key]
                self.removeNode(node)
            new_node = Node(key, value)
            self.hashmap[key] = new_node
            self.insertafterhead(new_node)


# Python specific implementation using hashmap and dict ordering

from collections import defaultdict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = defaultdict(int)

    def get(self, key: int) -> int:
        if key in self.hashmap:
            value = self.hashmap[key]
            del self.hashmap[key]
            self.hashmap[key] = value
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            del self.hashmap[key]
            self.hashmap[key] = value
        else:
            self.hashmap[key] = value

        if len(self.hashmap) > self.capacity:
            key2, val = next(iter(self.hashmap.items()))
            del self.hashmap[key2]
