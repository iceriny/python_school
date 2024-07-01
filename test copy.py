# Linked List
import enum
from hmac import new


class ListNode:
    def __init__(self, data, next: "ListNode | None" = None):
        self.data = data
        self.next: ListNode | None = next
        self.prev: ListNode | None = None

    def __str__(self):
        return f"{self.data} >> {self.next}"


class DoublyLinkedList:
    def __init__(self) -> None:
        self._items = set()
        self.head: ListNode | None = None

    def __len__(self):
        return len(self._items)

    def append(self, value):
        new_node = ListNode(value)
        self._items.add(new_node)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def insert_at_beginning(self, value):
        new_node = ListNode(value, self.head)
        if self.head is None:
            self.head = new_node
        else:
            self.head.prev = new_node
        self._items.add(new_node)
        self.head = new_node

    def insert_of_index(self, value, index):
        if index < 0 or index > len(self._items):  # 插入位置不合法
            raise IndexError("Index out of range")
        if index == 0:
            self.insert_at_beginning(value)
            return
        if index == len(self._items):
            self.append(value)
            return

        new_node = ListNode(value)
        self._items.add(new_node)
        curr = self.head
        prev = None
        current_pos = 0

        # 寻找插入位置的前一个节点
        while curr and current_pos < index:
            prev = curr
            curr = curr.next
            current_pos += 1

        if prev is None:  # 插入位置为第一个节点
            new_node.next = self.head
            self.head = new_node
            self.prev = new_node
            return

        prev.next = new_node
        new_node.prev = prev
        new_node.next = curr
