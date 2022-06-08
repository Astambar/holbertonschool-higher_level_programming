#!/usr/bin/python3
"""[summary]

Returns:
    [type]: [description]
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """[summary]

    Args:
        Rectangle ([type]): [description]
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        The __init__ function is called automatically every time
        the class is being used to create a new object.
        The init function can have arguments but the first
        one has to be self, which refers to the object itself.

        :param self: Reference the class itself
        :param size: Define the size of the square
        :param x=0: Set the x coordinate of the rectangle
        :param y=0: Set the y coordinate of the rectangle
        :param id=None: Assign a value to the id attribute
        :return: A rectangle object
        :doc-author: Trelent
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        The __str__ function is a special function
        that is called by the print()
        command. It returns a string representation
        of the object. This is useful for
        debugging and logging, but also allows
        objects to be used in place of strings!


        :param self: Refer to the object itself
        :return: A string that can be printed
        :doc-author: Trelent
        """

        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            __class__.__name__,
            self.id,
            self.x,
            self.y,
            self.size,
            )

    def update(self, *args, **kwargs):
        """
        The update function accepts 4 arguments:
            id, size, x and y.
            It changes the attributes of
            the object to match these values.


        :param self: Refer to the object itself
        :param *args: Pass a non-keyworded, variable-length argument list
        :param **kwargs: Pass a keyworded, variable-length argument list
        :return: Nothing
        :doc-author: Trelent
        """

        arg_list = ["id", "size", "x", "y", "\0"]

        if (len(args)):
            for i in range(len(args)):
                setattr(self, arg_list[i], args[i])

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        The to_dictionary function converts a
        list of lists into a dictionary.
        The first element in the list is used as
        the key, and the second as value.


        :param self: Reference the class itself
        :return: A dictionary representation of the object
        :doc-author: Trelent
        """

        return {'id': self.id, 'x': self.x, 'y': self.y, 'size': self.size}

    @property
    def size(self):
        """
        The size function returns the number of nodes in a linked list.

        Parameters:
            self (LinkedList): The current object referencing this method.

            Returns:
                int: The size of the linked list.

            Examples:

                &gt;&gt;&gt; ll = LinkedList() # Create a new

        :param self: Represent the instance of the object itself
        :return: The number of nodes in the linked list
        :doc-author: Trelent
        """

        return self.width

    @size.setter
    def size(self, value):
        """
        The size function sets the width of the rectangle.



        :param self: Access variables that belongs to the class
        :param value: Set the width of the rectangle
        :return: The width of the rectangle
        :doc-author: Trelent
        """

        self.see_value("width", value)
        self.width = value
        self.height = value
