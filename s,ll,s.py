class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListSlicer:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def slice(self, start, end):
        if start < 0:
            start = 0
        if end < 0:
            end = 0

        current = self.head
        count = 0
        sliced_list = LinkedListSlicer()

        while current and count < end:
            if count >= start:
                sliced_list.append(current.data)
            current = current.next
            count += 1

        return sliced_list

linked_list = LinkedListSlicer()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)


sliced_linked_list = linked_list.slice(1, 3)

current = sliced_linked_list.head
while current:
    print(current.data)
    current = current.next
