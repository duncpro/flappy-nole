# Flappy Nole (FSU Into to Python Project)
Flappy Nole is an FSU themed arcade game that is built in Python3 using PyGame.
Our inspiration came from the game Flappy Bird.

## Screen Capture
 ![FlappyNole Demo](./readme-assets/demo-video.gif)

## Libraries
pygame

pygame_gui

# Contributors
The following is a basic outline of the contributions made by each author. See the included git log for complete attribution.
## Taylor
### Vertical Movement
Taylor designed the system which is used to position the player vertically over time. The system inclues the concept of a Gravity constant which is added to the player's vertical momentum each tick. The effect being the player's speed of descent increases as time progresses, unless of course the player jumps.
### Graphics
Taylor designed the graphics used for pipes and the game background.
### Main Menu and User Accounts
Taylor developed the main menu, the sign-up screen, and the user account management system.

## Garrett
### Graphics
Worked on the original back ground graphics and edited main logo to work with hitboxes

### Movement
Worked to make game play smooth and close to the original game

### Scoring
Worked on saving highscore, storage and display to only save high score


## Duncan 
### Horizontal World Movement and Pipes
Duncan designed and developed the horizontal world space mechanism. Pipes are placed accross the horizontal wordspace at a constant rate such that the pipes are equadistant to each other. Pipe placement is determiend using a frequency constant
and modular arithmetic. 

### Circular Hitbox and Pipe Hitboxes
Utilized pygame to create a mesh of the Seminole Head which is used for collision detection between rectangular Pipe hitboxes. 

### Scoring
Duncan developed the score calculation algorithm. The score is a function of the number of pipes currently spawened in the world, the player's position, and the total number of pipes which have ever existed (spawned or not) within the world.

### Application Architecture
Duncan designed the main project structure. The app is built in a reactive style, where changes to the state are seperated from the actual rendering of the game. The main game loop is split into three phases.
1. Handle User Input
2. Handle Side Effects (progress the game forward through time)
3. Draw the Game State to the Screen

# Instructions for use
1. Make sure pygame and pygame_gui are installed.

2. Then run `python3 main.py` in the project directory.

3. Create a login using a unique username. When playing, use space bar to "jump".

# Video Explanation
https://youtu.be/J7QlzxYD1_o

## Resources
#### Images
Inspiration for background image and pipes - https://csw.fsu.edu/100years

Player icon - [https://upload.wikimedia.org/wikipedia/en/...](https://upload.wikimedia.org/wikipedia/en/thumb/d/d5/Florida_State_Seminoles_logo.svg/350px-Florida_State_Seminoles_logo.svg.png)

#### Game Inspiration
Flappy Bird - https://flappybird.io/
#### Materials

Python Docs - https://docs.python.org/3/

PyGame Docs - https://realpython.com/pygame-a-primer/

PyGame Tutorials - https://realpython.com/pygame-a-primer/

PyGame_GUI Docs - https://pygame-gui.readthedocs.io/en/latest/



