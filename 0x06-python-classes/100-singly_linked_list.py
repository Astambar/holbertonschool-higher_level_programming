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
        """
        The sorted_insert function takes a value and inserts it into the linked list in order.
        If the value is less than or equal to the current node, then it will be inserted at 
        the head of the list. If not, then we iterate through until we find a node whose data 
        is greater than our newNode's data.

        :param self: Reference the class itself
        :param value: Store the value of the new node to be inserted
        :return: The head of the list after insertion
        :doc-author: Trelent
        """

        newNode = Node(value)
        current = self.__head
        if (not current or value < current.data):
            if current:
                newNode.next_node = current
            self.__head = newNode
        else:
            while current.next_node and not (current.next_node.data >= value):
                current = current.next_node
            newNode.next_node = current.next_node
            current.next_node = newNode

    def __str__(self):
        """
        The __str__ function is a special function that is called by the str()
           built-in function and by the print statement to compute the &quot;informal&quot; string
           representation of an object. This is usually the string that you would type to 
           re-create this object.
        
        :param self: Refer to the object that is calling the method
        :return: A string representation of the linked list
        :doc-author: Trelent
        """
        
        res = ""
        current = self.__head
        while (current):
            res += str(current.data)
            if (current.next_node):
                res += '\n'
            current = current.next_node
        return res
