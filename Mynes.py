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
    game_board (MynesBoard): the board that is being played on
    screen (pygame.display): uses the screen from MynesGUI
    flag_count (int): Keeps track of how many flags the player has available to place
    clock (pygame.time): The time that the user has taken to play the game
    width (int): the width of the board, in pixels
    height (int): the height of the board, in pixels

    === Private Attributes ===
    _running (bool): whether the game is running or should be stopped
    _win (bool): whether the game has been won
    _lost (bool): whether the game has been lost
    """

    # ---------Mynes methods--------- #
    def __init__(self, mode: str):
        """
        Create a Mynes game that has a list of players (mines, numbers,
        empty spaces, etc)
        """
        self._win, self._running, self._lost = False, False, False
        self.game_board = MynesBoard(mode)
        self.screen = None
        self.flag_count = self.game_board.mine_count
        # Windows size in pixels
        self.width, self.height = self.game_board.width * ICON_SIZE, \
                                  self.game_board.height * ICON_SIZE
        self.clock = None

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

    def open_multiple(self, x: int, y: int) -> None:
        """
        It is used to open multiple squares at once. It recursively opens
        the block which is adjacent to the clicked square without a value
        attribute of 0

        :param x: height
        :param y: width
        """
        # Base cases
        if not self.game_board.inbound(x, y):
            return
        square = self.game_board.board[x][y]
        # To check if square is a bomb
        if square.value == -1:
            return
        # To check if already open or not
        if square.opened:
            return
        if square.flag:
            self.flag_count += 1
        square.open()
        # To check if square is a numbered one
        if square.value > 0:
            return
        # Recursive case
        # To check in all direction
        for (dx, dy) in [(0, 1), (0, -1), (1, 1), (1, -1), (1, 0), (0, 1),
                         (-1, 1), (-1, -1)]:
            self.open_multiple(x+dx, y+dy)

    def check_win_condition(self) -> None:
        """
        It check for the win condition i.e.: if all the squares with mines
        are flagged
        """
        self._win = True
        # To check if all the blocks with bomb are flagged or not
        for (board_x, board_y) in self.game_board.mine_lst:
            square = self.game_board.board[board_x][board_y]
            if not square.flag:
                # if not all are flagged then the self._win = False
                self._win = False
        # If won then display the win message
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
            ((self.width, self.height + 70), pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        clock = pygame.time.Clock()
        self.clock = clock

    def flag_counter(self) -> None:
        """
        Draws a rectangle under the game board. The rectangle contains text
        that reveals how many (correct) flags the user must place to win the
        game.
        """
        font = pygame.font.Font("freesansbold.ttf", 18)
        display_text = "Flags Remaining: " + str(self.flag_count)
        text_surface = font.render(display_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.width / 2, self.height + 20))
        pygame.draw.rect(self.screen, (0, 0, 0), text_rect, 20)
        self.screen.blit(text_surface, text_rect)

        pygame.display.update()

    def on_event(self, event: pygame.event) -> None:
        """
        React to the given <event> as appropriate.  Either the player makes a
        move or quits the game.
        """
        if event.type == pygame.QUIT:
            self._running = False
        # Player clicks when game is lost
        elif event.type == pygame.MOUSEBUTTONUP and (self._lost or self._win):
            self._running = False
        # Player clicks when game is running
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
        minutes = 0
        seconds = 0
        milliseconds = 0

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
                if not self._win:
                    self.render()
            if not self._win and not self._lost:
                if milliseconds > 1000:
                    seconds += 1
                    milliseconds -= 1000

                if seconds > 60:
                    minutes += 1
                    seconds -= 60

                # Adding time and rendering it to screen
                milliseconds += self.clock.tick_busy_loop(60)
                font = pygame.font.Font("freesansbold.ttf", 18)
                display_text = "Time: " + "{} : {}".format(minutes, seconds)
                text_surface = font.render(display_text, True, (255, 255, 255))
                text_rect = text_surface.get_rect(
                    center=(self.width / 2, self.height + 50))
                pygame.draw.rect(self.screen, (0, 0, 0), text_rect, 20)
                self.screen.blit(text_surface, text_rect)

                pygame.display.update()

        self.quit()
