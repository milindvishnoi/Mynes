import pygame
from Mynes import Mynes

BLACK = (0, 0, 0)
RED = (228, 57, 20)
WHITE = (255, 255, 255)
class MainWindow:
    """This is the main window of the game this window is displayed when
    the game begins. You can choose the difficulty of game here.

    === Attributes ===
    screen (pygame.display): uses the screen from MynesGUI
    clock (pygame.time): The time that the user has taken to play the game
    width (int): the width of the board, in pixels
    height (int): the height of the board, in pixels

     === Private Attributes ===
    _running (bool): whether the game is running or should be stopped
    """

    # ---------MainWindow methods--------- #
    def __int__(self):
        self._running = False
        self.width = 800
        self.height = 800
        self.screen = None
        self.clock = None

    # ---------Pygame Methods---------- #

    def on_init(self) -> None:
        """
        Initialize the game's main screen, and runs the initializer
        """
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800),
                                              pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.clock = pygame.time.Clock()
        self.screen.fill(WHITE)
        self.draw_buttons("Select the Game Mode", 400, 300, WHITE)
        self.draw_buttons("Easy", 400, 400, RED)
        self.draw_buttons("Medium", 400, 500, RED)
        self.draw_buttons("Hard", 400, 600, RED)
        self._running = True

    def on_event(self, event: pygame.event) -> None:
        """
        React to the given <event> as appropriate. Either the player selects
        a game mode or quits the game.
        """
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            temp_str = self.check_which_button(pos)
            if temp_str in ["Easy", "Medium", "Hard"]:
                self._running = False
                mynes = Mynes(temp_str)
                mynes.execute()

    def check_which_button(self, pos: list) -> str:
        """
        It checks which button is clicked.

        :param pos: It is teh position of the click on the screen
        :return: returns the name of teh button clicked/ if none of the
                buttons are clicked then returns nothing
        """
        if pos[0] > 353 and pos[0] < 446:
            if pos[1] > 380 and pos[1] < 420:
                return "Easy"
        if pos[0] > 324 and pos[0] < 475:
            if pos[1] > 480 and pos[1] < 518:
                return "Medium"
        if pos[0] > 352 and pos[0] < 473:
            if pos[1] > 580 and pos[1] < 618:
                return "Hard"

    def draw_buttons(self, text: str, width: int, height: int,
                     color: str) -> None:
        """
        It is used to create the buttons we need to start the game with.

        :param text: It is the text you want to display on the button
        :param width: Specifics the width placement of the button
        :param height: Specifics the height placement of the button
        :param text: Specifies the background color of the button
        """
        font = pygame.font.Font('freesansbold.ttf', 40)
        message = font.render(text, True, BLACK, color)
        popup_box = message.get_rect()
        popup_box.center = (width, height)
        self.screen.blit(message, popup_box)
        pygame.display.flip()

    def quit(self) -> None:
        """
        Clean up and close the game.
        """
        pygame.quit()

    def execute(self) -> None:
        """
        This runs the main window of the game.
        """
        self.on_init()
        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            pygame.display.update()
        self.quit()
