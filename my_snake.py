
def up():
    global direction
    direction = UP
    print('You pressed the up key')
def down():
    global direction
    direction = DOWN
    print('You pressed the down key')
def left():
    global direction
    direction = LEFT
    print('You pressed the left key')
def right():
    global direction
    direction = RIGHT
    print('You pressed the right key')

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if direction == RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print('You moved right!')
    elif direction == LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print('You moved left!')
    elif direction == UP:
        snake.goto(x_pos, y_pos+ SQUARE_SIZE)
        print('You moved up!')
    elif direction == DOWN:
        snake.goto(x_pos, y_pos- SQUARE_SIZE)
        print('You moved down!')
    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)

    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    if new_x_pos >= RIGHT_EDGE:
        print("you hit the right edge! game over!")
        quit()
    if new_x_pos <= LEFT_EDGE:
        print("you hit the left edge! game over!")
        quit()
    if new_y_pos >= UP_EDGE:
        print("you hit the right edge! game over!")
        quit()
    if new_y_pos <= DOWN_EDGE:
        print("you hit the left edge! game over!")
        quit()   

    turtle.ontimer(move_snake,TIME_STEP)
#####################################
    

import turtle
import random

turtle.tracer(1,0)

SIZE_X = 800
SIZE_Y = 500
turtle.setup(SIZE_X, SIZE_Y)

turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 6

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

# Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up postions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape('square')

turtle.hideturtle()

for num in range(START_LENGTH):
    x_pos = snake.pos()[0]
    y_pos = snake.pos()[1]
    x_pos += SQUARE_SIZE
    my_pos = (x_pos,y_pos)
    snake.goto(x_pos,y_pos)
    pos_list.append(my_pos)
    stamp_new = snake.stamp()
    stamp_list.append(stamp_new)

UP_ARROW = 'Up'
LEFT_ARROW = 'Left'
RIGHT_ARROW = 'Right'
DOWN_ARROW = 'Down'
TIME_STEP = 100
SPACEBAR = 'space'

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
direction = UP
turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.listen()
move_snake()

turtle.mainloop()
