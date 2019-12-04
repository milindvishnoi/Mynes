# Main file for Mynes Game project
# Controls the game state based on player inputs and updates MynesBoard

from MynesBoard import *
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
        self.screen = None
        self.flag_count = self.game_board.mine_count
        # Windows size in pixels
        self.width, self.height = self.game_board.width * ICON_SIZE, \
                                  self.game_board.height * ICON_SIZE

    def flagging(self, square):
        """
        Responsible to display/remove flag on square. It also decided if
        we need to flag or unflag. This function is also responsible to
        restrict the number of flags to be equal to number of bombs.

        :param square: it is the square we are checking for
        """
        if not square.opened:
            if self.flag_count > 0 and not square.flag:
                square.flagging()
                self.flag_count -= 1
            elif square.flag:
                square.unflagging()
                self.flag_count += 1

    def show_bombs(self) -> None:
        """
        Opens the whole board revealing all the mines and numbers
        """
        for board_x, board_y in self.game_board.mine_lst:
            square = self.game_board.board[board_x][board_y]
            square.open()
        self.render()

    def open_multiple(self, x, y) -> None:
        """
        It is used to open multiple squares at once. It recursively opens
        the block which is adjacent to the clicked square without a value
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
        if square.flag:
            self.flag_count += 1
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
            ((self.width, self.height + 40), pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.flag_counter()

    def flag_counter(self) -> None:
        """
        Draws a rectangle under the game board. The rectangle contains text
        that reveals how many (correct) flags the user must place to win the
        game.
        """
        font = pygame.font.Font("freesansbold.ttf", 18)
        display_text = "Flags Remaining: " + str(self.flag_count)
        text_surface = font.render(display_text, True, (255,255,255))
        text_rect = text_surface.get_rect(center=(self.width /2, self.height + 20))
        pygame.draw.rect(self.screen, (0,0,0), text_rect, 20)
        self.screen.blit(text_surface, text_rect)

        pygame.display.update()


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
                            self.on_left_click(square, board_x, board_y)
                        # Right click for Flagging
                        elif event.button == 3:
                            self.flagging(square)
                            self.check_win_condition()
                            self.flag_counter()
        self.flag_counter()

    def on_left_click(self, square, board_x, board_y) -> None:
        """
        Opens multiple square if square is 0 and opens only one square
        if square is numbered. It also finishes the game if the clicked square
        is a mine
        """
        if not square.flag:
            if square.value == 0:
                self.open_multiple(board_x, board_y)
            else:
                square.open()
        if square.value == -1:
            self.show_bombs()
            self.end_game_message()
            self._lost = True
        self.check_win_condition()

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
