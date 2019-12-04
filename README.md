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
<<<<<<< HEAD

## <a name="controls"></a>Controls
---
Left Click --> Reveal squares
[left_click_img](#/Pod7/left_click.png)


[Back To The Top](#Mynes)
## <a name="how-to-install"></a> How to Install
---

[Back To The Top](#Mynes)
## <a name="structure"></a> Project Structure
---

[Back To The Top](#Mynes)
## <a name="extend-the-game"></a>Extend the Game
---

[Back To The Top](#Mynes)
=======
Mynes is a game where you need to use logic to find out all the underlying mines. We remake Minesweeper and create a simpler version for beginners to Minesweeper. In the game window, there exist three different kinds of items: mines, numbers and flag. The rule is similar to minesweeper: you need to reveal all the number squares and flag all the mines. 

## <a name="controls"></a>Controls
---
* Left Click --> Reveal squares

* Right Click --> Flag squares

* After you flag all the mines, if the game finds that you flag some of the numbers, not mines, lose message will show up. If you left click on mines, lose message will also show up.

* If all flags correspond to all mines, win message will show up. 


[Back To The Top](#Mynes)
## <a name="how-to-install"></a> How to Install
---

[Back To The Top](#Mynes)
## <a name="structure"></a> Project Structure
---

[Back To The Top](#Mynes)
## <a name="extend-the-game"></a>Extend the Game
---

[Back To The Top](#Mynes)
>>>>>>> Yang
## <a name="individual-contributions"></a>Individual Contributions
---
* Milind Vishnoi: 
I did...

* Arjun Ganguly: 
I did...

<<<<<<< HEAD
* Ivy Zhang: 
I did...
=======
* Yang Zhang: 
I created the timer feature and fixed the win message bug. And I reorganized the game window to show the flag counter and timer. The timer starts when the pygame is run, and keep running until the player loses or wins the game. Then I placed timer and flag counter at the bottom of the pygame window. The win message cannot show up because pygame.display.flip() is called twice after the player wins. I fixed this bug and also created a few test cases for MyneSquare and MyneBoard. Finally, I completed description and controls for my game.
>>>>>>> Yang

* Justin Paglia: 
I did...

* Min Hyeok Lee: 
Through out the project I have Created "open() and flagging()" method in MyneSquare.py. The "open()" method detects the mouse event and changes the state of square by revealing what is inside. The "flagging()" is to place a flag on the square to remind that the square is a mine. Also in MynesBoard.py, I added the number initialization after placing mynes. It iterates through all the squares on the board and counts the number of mynes surrounding that square. Therefore, when the myne game is initiated, board with mynes and numbers are initialized. Lastly, I have created the license.md for our project


[Back To The Top](#Mynes)
## <a name="licence-information"></a>Licence Information
---
The MIT License (MIT)

Copy right © 2019 Pod7

You can find a copy of the License at file <tt>LICENSE</tt>

License for them is in <tt>Public Domain</tt>

[Back To The Top](#Mynes)
