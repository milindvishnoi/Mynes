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
        Create a code base board for Mynes, size and mine count is based on difficulty.
        (0,0) is the top-left of the board.

        """
        # Board size in playable spaces
        self.width = 8
        self.height = 8
        self.mine_count = 10
        # Construct board of empty squares
        self.board = [[
            MyneSquare(0, False, "temp_empty.png", pygame.Rect(x * ICON_SIZE, y * ICON_SIZE, ICON_SIZE, ICON_SIZE))
            for y in range(self.height)] for x in range(self.width)]
        # Place mines randomly on the squares
        i = 0
        while i < self.mine_count:
            mine_x, mine_y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            # Prevent duplicate mines
            if self.board[mine_y][mine_x].value != -1:
                self.board[mine_y][mine_x].value = -1
                self.board[mine_y][mine_x].icon = pygame.image.load("temp_empty.png")
                i += 1

