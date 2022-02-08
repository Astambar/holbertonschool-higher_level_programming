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
        """[summary]

        Args:
            size ([type]): [description]
            x (int, optional): [description]. Defaults to 0.
            y (int, optional): [description]. Defaults to 0.
            id ([type], optional): [description]. Defaults to None.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            __class__.__name__,
            self.id,
            self.x,
            self.y,
            self.size,
            )

    def update(self, *args, **kwargs):
        """[summary]
        """
        arg_list = ["id", "size", "x", "y", "\0"]

        if (len(args)):
            for i in range(len(args)):
                setattr(self, arg_list[i], args[i])

        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dictionary(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return {'id': self.id, 'x': self.x, 'y': self.y, 'size': self.size}
