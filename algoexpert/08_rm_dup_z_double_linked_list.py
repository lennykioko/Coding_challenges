class Node:
    def __init__(self, value=None, prev_node=None, next_node=None):
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node

    def __repr__(self):
        return f'<N {self.value}>'


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = new_node

    def __repr__(self):
        nodes = []
        current = self.head

        while current is not None:
            if current is self.head:
                nodes.append(f'H{current}')
            elif current.next_node is None and current is not self.head:
                nodes.append(f'{current}T')
            else:
                nodes.append(f'{current}')

            current = current.next_node

        return ' <-> '.join(nodes)


mylinked = DoubleLinkedList()
mylinked.add(1)
mylinked.add(1)
mylinked.add(3)
mylinked.add(4)
mylinked.add(4)
mylinked.add(4)
mylinked.add(5)
mylinked.add(6)
mylinked.add(6)

print(mylinked)


def removeduplicates(linked_list):
    """
    O(n) Time
    O(1) Space
    """
    current = linked_list.head

    while current is not None:
        next_distinct_node = current.next_node
        while next_distinct_node is not None and current.value == next_distinct_node.value:
            next_distinct_node = next_distinct_node.next_node

        current.next_node = next_distinct_node
        if next_distinct_node is not None:
            next_distinct_node.prev_node = current
        current = current.next_node

    return linked_list


removeduplicates(mylinked)
print(mylinked)
