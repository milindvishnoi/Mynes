# Main file for Mynes Game project
# Controls the game state based on player inputs and updates MynesBoard

from MynesBoard import *
# from MyneGUI import *
import pygame

WHITE = (0, 0, 0)
BLACK = (0, 0, 0)
ICON_SIZE = 25



class Mynes:
    """
    This class is the main running Mynes game.

    === Attributes ===
    screen: uses the screen from MynesGUI
    board: uses the board from MyneBoard
    flag_count: Keeps track of how many flags the player has available to place

    """

    # === Private Attributes ===
    # _running: pygame attribute that runs or stops the game
    # _flags_placed: Keeps track of how many flag objects are on the board

    game_board: MynesBoard
    # GUI: MynesGUI
    flag_count: int
    _running: bool

    # ---------Mynes methods--------- #
    def __init__(self):
        """
        Create a Mynes game that has a list of players (mines, numbers, empty spaces, etc)
        """
        self._running = False
        self._lost = False
        self.game_board = MynesBoard()
        # self.GUI = MynesGUI()
        self.screen = None
        self.flag_count = self.game_board.mine_count
        # Windows size in pixels
        self.width, self.height = self.game_board.width * ICON_SIZE, self.game_board.height * ICON_SIZE

    def get_number(self, x, y) -> int:
        """
        :param x: x-coordinate on board
        :param y: y-coordinate on board
        :return: Number at (x,y) on the board.
        """
        return self.board[x][y].number

    def get_flag(self, x, y) -> bool:
        """
        :param x: x-coordinate on board
        :param y: y-coordinate on board
        :return: If a flag is placed at (x,y) on the board.
        """
        return self.board[x][y].flagged

    def mynes_won(self) -> bool:
        """
        :return: If player has won the game by flagging all mines.
        """
        if self.flag_count > 0:
            return False
        else:
            x = 0
            y = 0
            for x in range(len(self.width)):
                for y in range(len(self.height)):
                    # Spot has mine but no flag
                    if (self.game_board.board[x][y].value == -1) and (self.game_board.board[x][y].flag == False):
                        return False

            return True

    def mynes_lost(self) -> None:
        """
        Mark the game as 'lost' if the player clicks a mine.
        """
        # Generate a fail message and text box to be printed in screen center
        font = pygame.font.Font('freesansbold.ttf', 16)
        fail_text = font.render("FAIL, CLICK TO EXIT", True, WHITE, BLACK)
        fail_box = fail_text.get_rect()
        fail_box.center = (self.width//2, self.height//2)

        self.screen.blit(fail_text, fail_box)
        pygame.display.flip()

        # End game
        self._lost = True

    # ---------Pygame Methods---------- #
    def on_init(self) -> None:
        """
        Initialize the game's screen, and begin running the game.
        """

        pygame.init()
        self.screen = pygame.display.set_mode \
            ((self.width, self.height), pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event: pygame.event) -> None:
        """
        React to the given <event> as appropriate.  Either the player makes a move or quits the game.
        """
        if event.type == pygame.QUIT:
            self._running = False
        # player clicks when game is lost
        elif event.type == pygame.MOUSEBUTTONUP and self._lost:
            self._running = False
        # player clicks when game is running
        elif event.type == pygame.MOUSEBUTTONUP:
            (x, y) = pygame.mouse.get_pos()
            # Loop through MyneSquare objects
            for board_y in range(self.game_board.height):
                for board_x in range(self.game_board.width):
                    square = self.game_board.board[board_x][board_y]
                    # Square that mouse is over
                    if square.hitbox.collidepoint(x, y):
                        # 1 for left click, 3 for right click
                        if event.button == 1:
                            if square.value == -1:
                                self.mynes_lost()
                            # else:
                            # self.board.clear_spaces
                            if square.value != -1:
                                square.icon = pygame.image.load(str(square.value) + ".png")
                                # self.mynes_lost()
                        # Right click for Flagging
                        elif event.button == 3:
                            # Remove Flag
                            if square.flag:
                                square.flag = False
                                self.flag_count += 1
                                square.icon = pygame.image.load("temp_empty.png")
                            # Don't Place Flag
                            elif (not square.flag) and self.flag_count == 0:
                                pass
                            # Place Flag
                            else:
                                square.flag = True
                                self.flag_count -= 1
                                square.icon = pygame.image.load("temp_flag.png")

    def quit(self) -> None:
        """
        Clean up and close the game.
        """

        pygame.quit()

    def render(self) -> None:
        """
        Call MynesGUI to render the pygame screen.
        """
        # Stop accepting player inputs when game is lost
        if not self._lost:
            font = pygame.font.Font('freesansbold.ttf', 12)
            for x in range(self.game_board.width):
                for y in range(self.game_board.height):
                    # number = font.render(str(self.game_board.board[x][y].value), True, WHITE, BLACK)
                    box = pygame.Rect(x * ICON_SIZE, y * ICON_SIZE, ICON_SIZE, ICON_SIZE)
                    # box = self.game_board.board[x][y].hitbox
                    self.screen.blit(self.game_board.board[x][y].icon, box)
            pygame.display.update()

    def execute(self) -> None:
        """
        Run the game until the game ends.
        """
        print("running")
        self.on_init()
        print("running")
        self.screen.fill(WHITE)
        while self._running:

            for event in pygame.event.get():
                self.on_event(event)
                self.render()

        self.quit()
