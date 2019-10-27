# Board Constructor and manipulator for Mynes

from typing import List
from MyneSquare import myne_square
import random
import pygame

ICON_SIZE = 24

class mynes_board:
    """
    === Public Attributes ===
    board:  Matrix representation of the board state, to be used by Mynes

    """

    # === Public Attributes ===
    # width: board width (right)
    # height: board height (down)
    # mine_count: number of mines placed on the board
    board: List[List]

    def __init__(self):
        """
        Create a code base board for Mynes, size and mine count is based on difficulty.
        (0,0) is the top-left of the board.

        """
        # Board size in playable spaces
        self.width = 8
        self.height = 8
        self.mine_count = 10
        # Construct board of empty squares
        self.board = [[
            myne_square(0, False, "temp_empty.png", pygame.Rect(x * ICON_SIZE, y * ICON_SIZE, ICON_SIZE, ICON_SIZE))
            for y in range(self.height)] for x in range(self.width)]
        # Place mines randomly on the squares
        i = 0
        while i < self.mine_count:
            mine_x, mine_y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            # Prevent duplicate mines
            if self.board[mine_y][mine_x].value != -1:
                self.board[mine_y][mine_x].value = -1
                self.board[mine_y][mine_x].icon = pygame.image.load("temp_mine.png")
                i += 1
        
        #Find number of adjacent mines for each non-myne square
        self.get_myne_values()
    
    def _get_adjacent_mynes(self, row: int, col: int) -> int:
        """Returns the number of mynes that are adjacent to a specific square coordinate
        on the board
        """

        # A list of column and row directions that should be checked for potential mynes
        rows_to_check = []
        cols_to_check = []

        # Considering the vertical edges of the board
        if row == 0:
            # Only consider curr row and row below
            rows_to_check = [1, 0]
        elif row == self.height - 1:
            # Only consider curr row and row above
            rows_to_check = [-1, 0]
        else:
            # Consider curr row, row above, and row below
            rows_to_check = [1, 0, -1]
        
        # Considering the horizontal edges of the board
        if col == 0:
            # Only consider curr col and col to the right
            cols_to_check = [1, 0]
        elif col == self.width - 1:
            # Only consider curr col and col to the left
            cols_to_check = [-1, 0]
        else:
            # Consider curr col, col to the left, and col to the right
            cols_to_check = [1, -1, 0]

        adjacent_mynes = 0      # Counter for number of adjacent mynes
        
        # Going through all adjacent rows
        for row_direction in rows_to_check:
            for col_direction in cols_to_check:
                # The exact coordinate to check
                x_coordinate = row + row_direction
                y_coorindate = col + col_direction

                # Getting value of square
                square = self.board[x_coordinate][y_coorindate]
                square_value = square.get_value()

                # Adding to myne counter if necessary
                if square_value == -1:
                    adjacent_mynes += 1
        
        return adjacent_mynes
        

    def get_myne_values(self) -> None:
        """Using the private helper method _get_adjacent_mynes(self, row: int, col: int)
        to update the value of non-myne squares as necessary
        """

        # Going through each coordinate of board
        for row in range(self.height):
            for col in range(self.width):
                # Getting value of square
                square = self.board[row][col]
                square_value = square.get_value()

                # Updating square value as necessary
                if square_value != -1:
                    adj_mynes = self._get_adjacent_mynes(row, col)
                    square.set_value(adj_mynes)


    def __str__(self) -> str:
        """String representation of <MynesBoard>, for user to view in console.

        Reminder that -1 represents a myne, 0 represents an empty space, and any other
        number represents the number of adjacment mines htat are present.

        >>> mynes_board = mynes_board()
        >>> print(mynes_board)
        [ 0 ][ 1 ][ 1 ][ 1 ][ 0 ][ 1 ][ 3 ][ -1]
        [ 0 ][ 1 ][ -1][ 1 ][ 0 ][ 1 ][ -1][ -1]
        [ 1 ][ 3 ][ 2 ][ 1 ][ 0 ][ 1 ][ 2 ][ 2 ]
        [ -1][ 2 ][ -1][ 1 ][ 0 ][ 0 ][ 0 ][ 0 ]
        [ 1 ][ 2 ][ 1 ][ 1 ][ 1 ][ 1 ][ 1 ][ 0 ]
        [ 0 ][ 0 ][ 0 ][ 0 ][ 1 ][ -1][ 1 ][ 0 ]
        [ 1 ][ 1 ][ 0 ][ 0 ][ 1 ][ 1 ][ 1 ][ 0 ]
        [ -1][ 1 ][ 0 ][ 0 ][ 0 ][ 0 ][ 0 ][ 0 ]
        """
        board = ''      # String that will represent the board

        # Going through the nested list representation of the Mynes board
        for row in self.board:
            for square in row:

                # Getting integer value of square
                square_value = square.get_value()

                # Adding to <board> as necessary
                if square_value == -1:
                    board += "[ -1]"
                else:
                    board += "[ " + str(square_value) + " ]"
            
            # Start new line for every row
            board += '\n'       
        
        return board
                

if __name__ == "__main__":
    mynes = mynes_board()
    print(mynes)
