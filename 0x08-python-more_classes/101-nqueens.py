#!/usr/bin/python3
"""_summary_

Returns:
	_type_: _description_
"""


import sys


if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        exit(1)
    numberQueen = int(sys.argv[1])
    if numberQueen < 4:
        print("N must be at least 4")
        exit(1)

    tableResult = []
    for i in range(numberQueen):
        tableResult.append([i, None])

    def cleartableResult(x):
        """
		The cleartableResult function clears the results table.
		
		
		
		:param x: Specify the number of rows that will be deleted from the table
		:return: The number of questions that were answered correctly
		:doc-author: Trelent
		"""
		
        for i in range(x, numberQueen):
            tableResult[i][1] = None

    def possible(x, y):
        """
		The possible function takes two parameters, x and y.
		It checks if the queen is in conflict with any other queen on the board.
		If it is in conflict, then it returns false. Otherwise, it returns true.
		
		:param x: Know the column of the queen that is trying to be placed
		:param y: Check if the queen is in a line with another one
		:return: A boolean value
		:doc-author: Trelent
		"""
		
        for z in range(numberQueen):
            if y == tableResult[z][1]:
                return False
        i = 0
        while(i < x):
            if abs(tableResult[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def nqueens(x):
        """
		The nqueens function takes a number of queens to be placed on the board as an argument.
		It then iterates through all possible positions for the first queen and places it in that position.
		If that placement is valid, it continues to place each successive queen in a valid position until 
		all queens have been placed successfully or there are no more possible placements.
		
		:param x: Indicate the row of the queen
		:return: A list of all the possible solutions for the nqueens problem
		:doc-author: Trelent
		"""
		
        for y in range(numberQueen):
            cleartableResult(x)
            if possible(x, y):
                tableResult[x][1] = y
                print(tableResult) if (x == numberQueen - 1) else nqueens(x + 1)
                    

    nqueens(0)
