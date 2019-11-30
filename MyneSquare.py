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
        :param flag: Boolean attribute for if a flag is placed on top of this square.
        """
        self.value = value
        self.flag = flag
        self.icon = pygame.image.load(icon)
        self.hitbox = hitbox
        self.opened = False

    def open(self):
        if self.value == -1 and self.opened == False :
            self.opened = True
            self.icon = pygame.image.load("mine.png")
        elif self.value != -1 and self.opened == False:
            self.opened = True
            self.icon = pygame.image.load(str(self.value) + ".png")

    def flagging(self):
        if self.flag == False and self.opened == False:
            self.flag == True
            self.icon = pygame.image.load("temp_flag.png")
        elif self.flag == True and self.opened == False:
            self.flag == False
            self.icon = pygame.image.load("temp_empty.png")
