# Board Constructor and manipulator for Mynes

from typing import List
from MyneSquare import MyneSquare
import random
import pygame

ICON_SIZE = 24

class MynesBoard:
    """
    === Public Attributes ===
    board:  Matrix representation of the board state, to be used by Mynes

    """

    # === Private Attributes ===
    # _width: board width (right)
    # _height: board height (down)
    # _mine_count: number of mines placed on the board
    board: List[List]

    def __init__(self):
        """
        Create a code base board for Mynes, size and mine count is based on
        difficulty.
        (0,0) is the top-left of the board.

        """
        # Board size in playable spaces
        self.width = 8
        self.height = 8
        self.mine_count = 10
        # Construct board of empty squares
        self.board = [[
            MyneSquare(0, False, "temp_empty.png",
                       pygame.Rect(x * ICON_SIZE, y * ICON_SIZE,
                                   ICON_SIZE, ICON_SIZE))
            for y in range(self.height)] for x in range(self.width)]
        self.place_mines()
        self.placing_numbers()

    def is_valid_coordinate(self, row, col) -> bool:
        """
        Checks if the coordinate is valid

        :return: if the coordinate is valid or not
        """
        if 0 <= row < self.width and 0 <= col < self.height:
            return True
        return False

    def place_mines(self) -> None:
        """
        It places the mines in the MynesBoard Randomly.

        :return: None
        """
        i = 0
        while i < self.mine_count:
            mine_x, mine_y = random.randint(0, self.width - 1), \
                             random.randint(0, self.height - 1)
            # Prevent duplicate mines
            if self.board[mine_y][mine_x].value != -1:
                self.board[mine_y][mine_x].value = -1
                self.board[mine_y][mine_x].icon = \
                    pygame.image.load("temp_mine.png")
                i += 1
        return None

    def placing_numbers(self) -> None:
        """
        Used to place number that indicate how many bombs are
        surrounding that block, this is done for the whole board.

        :return: None
        """
        for row in range(self.height):
            for col in range(self.width):
                # Prevents placing a number on a previously placed mine
                if self.board[row][col] != -1:
                    count = self.checking_directions(row, col)
                    self.board[row][col] = count

    def checking_directions(self, row, col) -> int:
        """
        checks all directions from a specific block and counts
        the number of blocks containing mines.
        :param row:
        :param col:
        :return:
        """
        count = 0
        directions = {-1, 0, 1}
        for drow in directions:
            for dcol in directions:
                if self.is_valid_coordinate(row + drow, col + dcol) and \
                        self.board[row + drow][col + dcol] == -1:
                    count += 1
        return count
