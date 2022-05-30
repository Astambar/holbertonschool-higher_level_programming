#!/usr/bin/python3
"""[summary]
"""


class MyInt(int):
    """[summary]

    Args:
        int ([type]): [description]
    """
    def __eq__(self, other):
        """[summary]

        Args:
            other ([type]): [description]

        Returns:
            [type]: [description]
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """[summary]

        Args:
            other ([type]): [description]

        Returns:
            [type]: [description]
        """
        return super().__eq__(other)
