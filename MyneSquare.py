import pygame


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

    def open_square(self):
        if self.value == -1:
            self.opened = True
            self.icon = pygame.image.load("temp_mine.png")
        else:
            self.opened = True
