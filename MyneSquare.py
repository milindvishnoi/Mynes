import pygame
from Mynes import *

class MyneSquare:
    """
    An object that acts as a playable space on the board.

    === Public Attributes ===
    value (int):  Value of the square; -1 is a Mine, 0 is an empty space, [1,8] are spaces with adjacent mines
    flag (bool): Whether this square is flagged
    icon (string): The .png file of the square
    hitbox (pygame.rect): Pygame rectangle for square
    """

    def __init__(self, value: int, flag: bool, icon: str, hitbox: pygame.rect):
        """
        Creates a new square object for the board.
        """
        self.value = value
        self.flag = flag
        self.icon = pygame.image.load(icon)
        self.hitbox = hitbox
        self.opened = False

    def open(self) -> None:
        """
        Opens that square by displaying the number/bomb in that block
        """
        if self.value == -1 and not self.opened:
            self.opened = True
            self.icon = pygame.image.load("Icons/mine.png")
        elif self.value != -1 and not self.opened:
            self.opened = True
            self.icon = pygame.image.load("Icons/" + str(self.value) + ".png")

    def flagging(self) -> None:
        """
        Used to display the flag on the square
        """
        if not (self.flag and self.opened):
            self.flag = True
            self.icon = pygame.image.load("Icons/temp_flag.png")

    def unflagging(self) -> None:
        """
        Used to remove a flag from a square
        """
        if self.flag and not self.opened:
            self.flag = False
            self.icon = pygame.image.load("Icons/temp_empty.png")
