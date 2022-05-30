#!/usr/bin/python3
"""[summary]
"""


class MyInt(int):
    """[summary]

    Args:
        int ([type]): [description]
    """
    def __eq__(self, others):
        """[summary]

        Args:
            others ([type]): [description]

        Returns:
            [type]: [description]
        """
        return super().__ne__(others)

    def __ne__(self, others):
        """[summary]

        Args:
            others ([type]): [description]

        Returns:
            [type]: [description]
        """
        return super().__eq__(others)
