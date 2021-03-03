from linked_list import LinkedList  # noqa


def merge_sort(linked_list):
    """
    Sorts a linked_list in ascending order
    Recursively divide the linked list into sublists containing a single node
    Repeatedly merge the sublists to produce sorted sublists until one remains

    Returns a new sorted linked list

    Takes O(kn log n) time
    """

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right

    Takes overall O(k log n) time
    """

    if linked_list is None or linked_list.head is None:
        left_half = linked_list
        right_half = None

        return left_half, right_half

    else:
        size = linked_list.size()
        midpoint = size // 2

        mid_node = linked_list.node_at_index(midpoint - 1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half


def merge(left, right):
    """
    Merges two linked lists, sorting by data in nodes
    Returns a new merged list

    Runs in overall O(n) time
    """

    # Create a new lined list that contains nodes from merging left and right
    merged = LinkedList()

    # Add a fale head that is discarded later
    merged.add(0)

    # set current to the head of the linked list
    current = merged.head

    # Obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head

    # Iterate over left and right until we reach the tail of either
    while left_head or right_head:
        # if the head node of left is None, we're past the tail
        # Add the noded from right to merged list
        if left_head is None:
            current.next_node = right_head
            # set next on right to set loop condition to False
            right_head = right_head.next_node

        # if the head node of right is None, we're past the tail
        # Add the noded from left to merged list
        elif right_head is None:
            current.next_node = left_head
            # set next on left to set loop condition to False
            left_head = left_head.next_node
        else:
            # Not at either tail node
            # Obtain node data to to perforrm comparison operations
            left_data = left_head.data
            right_data = right_head.data

            # if data on left is less than right, set current to left node
            if left_data < right_data:
                current.next_node = left_head
                # Move left head to next node
                left_head = left_head.next_node
            # if data on left is greater than right, set current to right node
            else:
                current.next_node = right_head
                # Move right head to next node
                right_head = right_head.next_node

        # Move current to next node
        current = current.next_node

    # Discard fake head and set first merged mode as head
    head = merged.head.next_node
    merged.head = head

    return merged


al = LinkedList()
al.add(10)
al.add(2)
al.add(44)
al.add(56)
al.add(15)
al.add(99)

print(al)
sorted_list = merge_sort(al)
print(sorted_list)
