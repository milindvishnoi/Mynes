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

    def get_value(self) -> int:
        """Returns the integer representation of the square

        >>> new_square = MyneSquare(0, False, "temp_empty.png", 
                            pygame.Rect(x * ICON_SIZE, y * ICON_SIZE, ICON_SIZE, ICON_SIZE))
                            for y in range(self.height)] for x in range(self.width)]
        >>> myne_quare.get_value()
        -1
        """
        return self.value
    

    def set_value(self, value:int) -> None:
        """Changes the value of the square to the paramater that is given.
        """
        self.value = value
