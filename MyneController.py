"""
Initializes and runs the Mynes game through pygame
"""
import pygame
from Mynes import Mynes
WHITE = (255, 0, 0)
BLACK = (255, 255, 255)
ICON_SIZE = 24


class MyneController(Mynes):
    """Run the main from this class to play the game myne"""

    def __init__(self) -> None:
        Mynes.__init__(self)


    def is_gameover(self) -> bool:
        "Go through all the board and checks if all the squares are opened"


    def on_init(self):
        """Initializes the game screen and runs the game"""
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height),
                                              pygame.HWSURFACE
                                              | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event: pygame.event) -> None:
        """
        Player makes a move or quits and system reacts to it.
        """
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.MOUSEBUTTONUP and self._lost:
            self._running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            (x, y) = pygame.mouse.get_pos()
            for board_y in range(self.game_board.height):
                for board_x in range(self.game_board.width):
                    square = self.game_board.board[board_x][board_y]
                    if square.hitbox.collidepoint(x, y):
                        if event.button == 1:
                            if square.value == -1: #-1 represents the myne
                                square.open_square()
                                self.mynes_lost()
                            else:
                                #returns the number corresponding to the square
                                square.open_square()
                        elif event.button == 3:
                            # Remove flag
                            if square.flag:
                                square.flag = False
                                self.flag_count += 1
                                square.icon = pygame.image.load("temp_empty.png")
                            # Don't place flag
                            elif (not square.flag) and self.flag_count == 0:
                                pass
                            # Place flag
                            else:
                                square.flag = True
                                self.flag_count -= 1
                                square.icon = pygame.image.load("temp_flag.png")

    def quit(self) -> None:
        """
        Clean up and close the game
        """
        pygame.quit()

    def render(self) -> None:
        """
        Call MynesGUI to render the pygame screen.
        """

        if not self._lost:
            font = pygame.font.Font('freesansbold.ttf', 12)
            for x in range(self.game_board.width):
                for y in range(self.game_board.height):
                    # number = font.render(str(self.game_board.board[x][y].value), True, WHITE, BLACK)
                    box = pygame.Rect(x * ICON_SIZE, y * ICON_SIZE, ICON_SIZE, ICON_SIZE)
                    # box = self.game_board.board[x][y].hitbox
                    self.screen.blit(self.game_board.board[x][y].icon, box)
            pygame.display.update()


if __name__ == "__main__":
    game = MyneController()
    game.on_init()
    game.screen.fill(WHITE)
    while game._running:
        for event in pygame.event.get():
            game.on_event(event)
            game.render()
    game.quit()








