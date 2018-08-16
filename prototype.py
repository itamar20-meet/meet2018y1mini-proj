import turtle
import random #We'll need this later in the lab

turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=1000
SIZE_Y=1000
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle windo
borders_size_x=500
borders_size_y=500
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 1


#Initialize listsmy
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
borders = turtle.clone()
snake = turtle.clone()
title = turtle.clone()
snake.shape("square")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for snake_length  in range(START_LENGTH+1) :
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1]

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+=SQUARE_SIZE

    my_pos=(x_pos,y_pos) #Store position variables in a tuple
    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
   
    #Append the new position tuple to pos_list
    pos_list.append(my_pos) 

    #Save the stamp ID! You'll need to erase it later. Then append
    # it to stamp_list.             
    snake_stamp1 = snake.stamp()
    stamp_list.append(snake_stamp1)


###############################################################
#                    PART 2 -- READ INSTRUCTIONS!!
###############################################################
UP_ARROW = "Up" #Make sure you pay attention to upper and lower 
                #case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many 
                #milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!

UP = 0
DOWN = 2
LEFT = 1
RIGHT = 3
#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!!

#Go to the top of your file, and after the line that says direction = UP,  write:
direction=UP

def left():
    global direction
    direction=LEFT
    print("You pressed the left key!")
    
def right():
    global direction
    direction=RIGHT#Change direction to up
    print("You pressed the right key!")
    

#2. Make functions down(), left(), and right() that change direction
####WRITE YOUR CODE HERE!!

 # Create listener for up key
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)

turtle.listen()
def move_snake():
    START_SIZE = 6
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    #Add new lines to the end of the function
    #Grab position of snake
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    # The next three lines check if the snake is hitting the 
    # right edge.
   
    

    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction==UP:
        snake.goto(x_pos ,y_pos + SQUARE_SIZE)
        print("You moved up!")
    elif direction==DOWN:
        snake.goto(x_pos,y_pos - SQUARE_SIZE)
        print("You moved down!")
move_snake


        




