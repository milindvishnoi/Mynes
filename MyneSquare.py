import pygame
from Mynes import *


class MyneSquare:
    """
    An object that acts as a playable space on the board.
    """

    def __init__(self, value: int, flag: bool, icon: str, hitbox: pygame.rect):
        """
        Creates a new square object for the board.
        :param value: Integer that tells Mynes what is on this square.
        -1 is a Mine, 0 is an empty space, [1,8] are spaces with adjacent mines
        :param flag: Boolean attribute for if a flag is placed on top of this
        square.
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
            self.icon = pygame.image.load("mine.png")
        elif self.value != -1 and not self.opened:
            self.opened = True
            self.icon = pygame.image.load(str(self.value) + ".png")

    def flagging(self) -> None:
        """
        Used to display the flag on the square
        """
        if not (self.flag and self.opened):
            self.flag = True
            self.icon = pygame.image.load("temp_flag.png")

    def unflagging(self) -> None:
        if self.flag and not self.opened:
            self.flag = False
            self.icon = pygame.image.load("temp_empty.png")
