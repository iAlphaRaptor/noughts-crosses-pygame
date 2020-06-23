# noughts-crosses-pygame

A simple noughts and crosses game made in python with the pygame package.

### main.py
The main program which runs the whole project and plays the game.

### input_boxes.py
A class which allows input boxes to be created for typed input.
Allows for customisation of:
* Background colour
* Text colour
* Input box colour
* Question text

### tile.py
A class which is called 9 times, once for each square in the grid. Used to detect when a square is clicked on and to display the pieces.

### win_check.py
Contains a single function, winCheck(), which checks if either player has won. Draws are handled by main.py.

### Fonts and Images
Contain the sources of the images and fonts used throughout the project.
