# Mynes
Pod7 coming up with a game Mynes, which inspired by Minesweeper 

---

## Navigation
- [Description](#description)
- [Controls](#controls)
- [How to Install](#how-to-install)
- [Project Structure](#structure)
- [Extend the Game](#extend-the-game)
- [Individual Contributions](#individual-contributions)
- [Licence Information](#licence-information)
---
## <a name="description"></a>Description
---
Mynes is a game where you need to use logic to find out all the underlying mines. We remake Minesweeper and create a simpler version for beginners to Minesweeper. In the game window, there exist three different kinds of items: mines, numbers and flag. The rule is similar to minesweeper: you need to reveal all the number squares and flag all the mines. 

## <a name="controls"></a>Controls
---
* Left Click --> Reveal squares ![](Icons/1.png) or ![](Icons/mine.png)
* Right Click --> Flag squares ![](Icons/temp_flag.png)
* After you flag all the mines, if the game finds that you flag some of the numbers, not mines, lose message will show up. If you left click on mines, lose message will also show up.
* If all flags correspond to all mines, win message will show up. 
* Flag counter will change every time you flag a mine.


[Back To The Top](#Mynes)
## <a name="how-to-install"></a> How to Install
---
To install the game you need to type this code into the terminal/cmd.

> pip install https://github.com/milindvishnoi/Pod7.git

This command will install the game to your computer, if it doesn't please contact me on milindvishnoi@gmail.com. 

Enjoy our game!

[Back To The Top](#Mynes)
## <a name="structure"></a> Project Structure
---
#### File Structure
* All code and github related files are stored in the project directory.
* All unit testing files are located in the "MyneTest" folder.
* All images used (0-8, empty, mine, and flag) are stored in the "Icons" folder.

![](Icons/mine.png)![](Icons/temp_empty.png)![](Icons/temp_flag.png)![](Icons/0.png)![](Icons/1.png)![](Icons/2.png)![](Icons/3.png)![](Icons/4.png)![](Icons/5.png)![](Icons/6.png)![](Icons/7.png)![](Icons/8.png)

That's it!

#### Code Structure
This is a breakdown of each file's methods and what they do, in the order that the files reference each other.  For a more specific description, check the code and docstrings.

1. **MynesLauncher:**   Simply has a main method that initializes and runs a new Mynes game. (This is so you can double-click to launch.)

2. **Mynes:**   This class is the main game class that handles most of the "front-end" functionality.
  * Initializes a new board for the game to be played on.
  * Calls a new pygame instance to be displayed, and recieve events from.
  * Keeps track of play time after the instance is created, and flag count while the game is running.
  * Handles events, but the only two that matter are left and right clicking:
    * Left click "Opens" (clears) squares when the player clicks on a certain MyneSquare.  If that square has a Myne, then all squares are revealed and the game is lost.  This calls `end_game_message()`.
    * Right click places a flag, calling `flagging()` and updating the appropriate square with a flag image.  If all Mynes are flagged after this event, `show_win_message()` will display the win message after the next click.
    
3. **MynesBoard:**   This board handles a matrix of MyneSquare objects that correspond to grid places, and the actions involving said squares.
* Mynes are placed randomly with `place_mine()` when the board is intialized.
* After the Mynes are placed, `place_numbers()` assigns each square a number basedon the amount of Mynes adjacent to that square.
* The board can also check is a given square coordinate is valid or not using `inbound()`.

4. **MyneSquare:**   These squares are an object representation of the board squares, making it easier to track where user clicks happen and what to do on such events.
* Each square has a rectangle hitbox object, which is used to detect user clicks.
* Each square has a value, which determines which icon it gets (-1 for Mynes, 0-8 for empty or adjacent squares).
* Each square has a flag attribute, which can be placed or removed with `flagging()` and `unflagging()` respectively.
* Each square can also be "opened" to reveal what is underneath it.

[Back To The Top](#Mynes)
## <a name="extend-the-game"></a>Extend the Game
---
All developers are encouraged to not only install and play this game, but to extend it as well. All source code is available for anyone who wishes to make any tweaks. Whether one wishes to make the game harder, make the game easier, or add more attractive animations, we want developers to have the ability to do so. Feel free to read through the project structure above to understand how the game works before adding any tweaks.


Some suggested tweaks:
* Making the game board larger
* Adding more mynes to the game board
* Creating different levels to make the game progressively harder
* Creative animation if a game is lost
* Ability to play the game using only a keyboard

Example:
Here is how one would make the game board larger and add more mines to the game. In [MynesBoard.py](MynesBoard.py), the initializer defines three specific attributes that can be changed to make the game easier or harder.

```Python
    def __init__(self):
        """
        Create a code base board for Mynes, size and mine count is based on difficulty.
        (0,0) is the top-left of the board.
        """
        # Board size in playable spaces
        self.width = 10 # Default value is 10, but can be changed to any number
        self.height = 10 # Default value is 10, but can be changed to any number
        self.mine_count = 10 # Default value is 10, but can be changed to any number
        ...
```

[Back To The Top](#Mynes)
## <a name="individual-contributions"></a>Individual Contributions
---
* Milind Vishnoi: 
I created the win_condition method. The purpose of this method is to close the execution of the application. The win_condition method checks to see if all the squares with the bombs are already flagged or not. Furthermore the  implementation of the multiple_open_square method was also done by me. The multiple_open_square method was implemented to recursively open multiple squares. This is done when the squares value is 0. If the value of the squares is equal to 0 then the recursion continues, if the value fails to equal 0 then it stops. 
Next off, I also fixed the functionality of other methods. There was no limit to flagging the number of sqaures. I made changes to the implementation of the flagging function, so that the number of flags would be equal to the number of bombs. Additionally a condition which would show all the bombs once the game ends was added aswell. Lastly, I also added a condition that restricted the user to only flag closed squares. 

* Arjun Ganguly: 
In the initial stages of the project, I made a string reperesentation of the board that can be displayed to the console. This made working on the game much easier when the Pygame implementation had not been done. I also created a method to determine the specific numbers that a square on the board should assume. Each number corresponds to how many mines are adjacent to a square. Once the pygame GUI was implemented, I made the number icons for the board. I generated the correct number on the GUI for each non-mine square on the game board. During the final stage of writing code, I created a working flag counter that displayed how many remaining flags the user must place in order to win the game. Finally, I wrote the "Extend the Game" section on the README.md file. I also formatted the README so that a user could navigate through the page by clicking section headings at the top of the file or "Back to the Top" at the end of a section. 

* Yang Zhang: 
I created the timer feature and fixed the win message bug. And I reorganized the game window to show the flag counter and timer. The timer starts when the pygame is run, and keep running until the player loses or wins the game. Then I placed timer and flag counter at the bottom of the pygame window. The win message cannot show up because pygame.display.flip() is called twice after the player wins. I fixed this bug and also created a few test cases for MyneSquare and MyneBoard. Finally, I completed description and controls for my game.

* Justin Paglia: 
I got carried away at the start of this project and set up basic versions of the four main classes (Mynes, MynesBoard, MyneSquare, MynesLauncher).  In Mynes I figured out how pygame launches, runs, and quits in order to get the game window working.  I also set up some event handling including the left and right click functions, as well as winning or losing the game (which has since been improved).

For MynesBoard, I wrote the basic board generator, which initializes the MyneSquare objects, and randomly places the mines.  The MyneSquares initializer was created by me as well.

MynesLauncher simply runs the game, and has remained unchanged.  I also made some temporary images to prove that the game was partially functional (myne, flag, and empty) which have since been updated.

* Min Hyeok Lee: 
Through out the project I have Created "open() and flagging()" method in MyneSquare.py. The "open()" method detects the mouse event and changes the state of square by revealing what is inside. The "flagging()" is to place a flag on the square to remind that the square is a mine. Also in MynesBoard.py, I added the number initialization after placing mynes. It iterates through all the squares on the board and counts the number of mynes surrounding that square and save as value in the square. Therefore, when the myne game is initiated, board with mynes and numbers are initialized. Lastly, I have created the license.md for our project


[Back To The Top](#Mynes)
## <a name="licence-information"></a>Licence Information
---
The MIT License (MIT)

Copy right © 2019 Pod7

You can find a copy of the License at file <tt>LICENSE</tt>

License for them is in <tt>Public Domain</tt>

[Back To The Top](#Mynes)
