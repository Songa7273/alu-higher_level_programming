#!/usr/bin/python3

class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        self._data = data
        self._next_node = next_node

    @property
    def data(self):
        """Retrieve the data attribute."""
        return self._data

    @data.setter
    def data(self, value):
        """Set the data attribute.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """Retrieve the next_node attribute."""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next_node attribute.

        Raises:
            TypeError: If value is not None or a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value

class SinglyLinkedList:
    """Defines a singly linked list."""

    def __init__(self):
        self._head = None

    def __str__(self):
        """Print the entire list in stdout."""
        current = self._head
        nodes = []
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return '\n'.join(nodes)

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list.

        Args:
            value (int): The value to be inserted.
        """
        new_node = Node(value)

        if self._head is None or value < self._head.data:
            new_node.next_node = self._head
            self._head = new_node
            return

        current = self._head
        while current.next_node and value > current.next_node.data:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
