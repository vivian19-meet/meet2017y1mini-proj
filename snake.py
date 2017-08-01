
import turtle
import random #We'll need this later in the lab
turtle.tracer(1,0) #This helps the turtle move more smoothly
SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window
#size.
turtle.penup()
SQUARE_SIZE = 20
START_LENGTH = 8
#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")
#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()


#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for i in range(START_LENGTH):
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1]
    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?
    # You're RIGHT!
    x_pos=SQUARE_SIZE +x_pos
    my_pos=(x_pos,y_pos) #Store position variables in a tuple
    snake.goto(x_pos,y_pos) #Move snake to new(x,y)
    #Append the new position tuple to pos_list
    pos_list.append(my_pos)
    #Save the stamp ID! You'll need to erase it later. Then append
    # it to stamp_list.
    stamp1 = snake.stamp()
    stamp_list.append(snake.stamp)

UP_ARROW = "Up" #Make sure you pay attention to upper and lower
#case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many
#milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!
UP = 0
#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!!
DOWN=1
LEFT=2
RIGHT=3
direction = UP
def up():
    global direction #snake direction is global (same everywhere)
    direction=UP #Change direction to up
    move_snake() #Update the snake drawing <- remember me later
    print("You pressed the up key!")
#2. Make functions down(), left(), and right() that change
def DOWN():
    global direction
    direction=DOWN
    move_snake()
    print("You pressed the down key!")
def RIGHT():
    global direction
    direction=RIGHT
    move_snake()
    print("You pressed the RIGHT key!")

def LEFT():
    global direction
    direction=LEFT
    move_snake()
    print("You pressed the LEFT key!")
    
    
####WRITE YOUR CODE HERE!!
    
turtle.onkeypress(up, UP_ARROW) # Create listener for up key
#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!
turtle.onkeypress(DOWN, DOWN_ARROW)
turtle.onkeypress(LEFT, LEFT_ARROW)
turtle.onkeypress(RIGHT, RIGHT_ARROW)
turtle.listen()
def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print('You moved right!')
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print('You moved left!')
    elif direction== UP:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print('You moved up!')
    else:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print('You moved down!')
#4. Write the conditions for UP and DOWN on your own
##### YOUR CODE HERE
#Stamp new element and append new stamp in list
#Remember: The snake position changed - update my_pos()
my_pos=snake.pos()
pos_list.append(my_pos)
new_stamp = snake.stamp()
stamp_list.append(new_stamp)
######## SPECIAL PLACE - Remember it for Part 5
#pop zeroth element in pos_list to get rid of last the last
#piece of the tail
old_stamp = stamp_list.pop(0)
snake.clearstamp(old_stamp)
pos_list.pop(0)
    
