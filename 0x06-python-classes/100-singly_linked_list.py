#!/usr/bin/python3
"""[summary]

    Raises:
    TypeError: [description]
    TypeError: [description]

    Returns:
    [type]: [description]
"""


class Node:
    """AI is creating summary for Node

    Raises:
        TypeError: [description]
        TypeError: [description]

    Returns:
        [type]: [description]
    """

    def __init__(self, data, next_node=None):
        """[summary]

        Args:
            data ([type]): [description]
            next_node ([type], optional): [description]. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__data

    @property
    def next_node(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__next_node

    @data.setter
    def data(self, value):
        """[summary]

        Args:
            value ([type]): [description]

        Raises:
            TypeError: [description]
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """[summary]

        Args:
            value ([type]): [description]

        Raises:
            TypeError: [description]
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """[summary]

    Returns:
        [type]: [description]
    """

    def __init__(self):
        """[summary]
        """
        self.__head = None

    def sorted_insert(self, value):
        """[summary]

        Args:
            value ([type]): [description]
        """
        newNode = Node(value)
        current = self.__head
        if (not current or value < current.data):
            if current:
                newNode.next_node = current
            self.__head = newNode
        else:
            while (current.next_node):
                if (current.next_node.data >= value):
                    break
                current = current.next_node
            newNode.next_node = current.next_node
            current.next_node = newNode

    def __str__(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        res = ""
        current = self.__head
        while (current):
            res += str(current.data)
            if (current.next_node):
                res += '\n'
            current = current.next_node
        return res
