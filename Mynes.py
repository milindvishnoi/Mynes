# Main file for Mynes Game project
# Controls the game state based on player inputs and updates MynesBoard

from tkinter import *
from MynesBoard import *
# from MyneGUI import *
import pygame

BLACK = (0, 0, 0)
RED = (228, 57, 20)
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
    _win: bool

    # ---------Mynes methods--------- #
    def __init__(self):
        """
        Create a Mynes game that has a list of players (mines, numbers,
        empty spaces, etc)
        """
        self._win, self._running, self._lost = False, False, False
        self.game_board = MynesBoard()
        # self.GUI = MynesGUI()
        self.screen = None
        self.flag_count = self.game_board.mine_count
        # Windows size in pixels
        self.width, self.height = self.game_board.width * ICON_SIZE, \
                                  self.game_board.height * ICON_SIZE

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

    def show_board(self) -> None:
        """
        Opens the whole board revealing all the mines and numbers
        """
        for board_y in range(self.game_board.height):
            for board_x in range(self.game_board.width):
                square = self.game_board.board[board_x][board_y]
                square.open()
        self.render()

    def open_multiple(self, x, y) -> None:
        """
        It is used to open multiple blocks at once. It recursively opens
        the block which is adjacent to the clicked block without a value
        attribute of 0

        :param x: height
        :param y: width
        """
        # base cases
        if not self.game_board.inbound(x, y):
            return
        square = self.game_board.board[x][y]
        # to check if square is a bomb
        if square.value == -1:
            return
        # to check if already open or not
        if square.opened:
            return
        square.open()
        # to check if square is a numbered one
        if square.value > 0:
            return
        # recursive case
        # to check in all direction
        for (dx, dy) in [(0, 1), (0, -1), (1, 1), (1, -1), (1, 0), (0, 1),
                         (-1, 1), (-1, -1)]:
            self.open_multiple(x+dx, y+dy)

    def check_win_condition(self) -> None:
        """
        It check for the win condition i.e.: if all the squares with mines
        are flagged
        """
        self._win = True
        # to check if all the blocks with bomb are flagged or not
        for (board_x, board_y) in self.game_board.mine_lst:
            square = self.game_board.board[board_x][board_y]
            if not square.flag:
                # if not all are flagged then the self._win = False
                self._win = False
        # if won then display the win message
        if self._win:
            self.show_win_message()

    def show_win_message(self) -> None:
        """
        The message we display if the player wins the game by calling the
        display_message method which is defined under pygame methods
        """
        self.display_message("You Won!!")

    def end_game_message(self) -> None:
        """
        The message we display if the player loses the game by calling the
        display_message method which is defined under pygame methods
        """
        self.display_message("Game Over")

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
        React to the given <event> as appropriate.  Either the player makes a
        move or quits the game.
        """
        if event.type == pygame.QUIT:
            self._running = False
        # player clicks when game is lost
        elif event.type == pygame.MOUSEBUTTONUP and (self._lost or self._win):
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
                            if square.value == 0:
                                self.open_multiple(board_x, board_y)
                            else:
                                square.open()
                            if square.value == -1:
                                self.show_board()
                                self.end_game_message()
                                self._lost = True
                        # Right click for Flagging
                        elif event.button == 3:
                            self.check_win_condition()
                            # Don't place Flag
                            if self.flag_count == 0:
                                continue
                            else:
                                square.flagging()
                                # placed flag
                                if square.flag:
                                    self.flag_count -= 1
                                # removed flag
                                else:
                                    self.flag_count += 1

    def quit(self) -> None:
        """
        Clean up and close the game.
        """
        pygame.quit()

    def display_message(self, text) -> None:
        """
        Method is used to display any message once game is over

        :param text: The string you want to display
        """
        font = pygame.font.Font('freesansbold.ttf', 20)
        message = font.render(text, True, BLACK, RED)
        popup_box = message.get_rect()
        popup_box.center = (self.width // 2, self.height // 2)
        self.screen.blit(message, popup_box)
        pygame.display.flip()

    def render(self) -> None:
        """
        Call MynesGUI to render the pygame screen.
        """
        # Stop accepting player inputs when game is lost
        if not self._lost:
            for x in range(self.game_board.width):
                for y in range(self.game_board.height):
                    box = pygame.Rect(x * ICON_SIZE, y * ICON_SIZE, ICON_SIZE,
                                      ICON_SIZE)
                    self.screen.blit(self.game_board.board[x][y].icon, box)
            pygame.display.update()

    def execute(self) -> None:
        """
        Run the game until the game ends.
        """
        self.on_init()
        self.screen.fill(BLACK)
        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
                self.render()
        self.quit()
