################## Pong Game #######################

Problem statement:
Create a pong game. With each hit from the paddle, the speed of the ball should increase

Solution:
1. Create a screen from turtle module (Screen Class)
    - Height: 600
    - Width: 800
    - Color: black
    - Exit On click
    - Title: Pong Game

2. Create two paddles and move the paddle as per the keystrokes
    - Shape: square
    - Height: 100
    - Width: 20
    - Position: (350, 0) and (-350, 0)
    - Moves as per the key strokes

3. Create a ball and make it move
    - Shape: circle
    - Width: 20
    - Height: 20
    - Initial_Position: (0,0)
    - 

4. Detect a collision with upper and lower wall and make it bounce
    - In bounce, the ball should reverse its y coordinates to bounce.

5. Detect a coolision with paddle and make it bounce

6. Detect when the paddle is missed

7. Maintain a scoreboard