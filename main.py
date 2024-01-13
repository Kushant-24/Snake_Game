from turtle import Turtle, Screen
from random import randint
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.tracer(0)
screen.listen()
screen.title("Snake Game by ks.negi")

'''All Fucntions Here'''

# Fucntions link to controlling keys
def up():
    if snake_head.heading() != 270:
        snake_head.setheading(90)
def down():
    if snake_head.heading() != 90:
        snake_head.setheading(270)
def right():
    if snake_head.heading() != 180:
        snake_head.setheading(0)
def left():
    if snake_head.heading() != 0:
        snake_head.setheading(180)

# Defining snake creation function
def snake(location):
    tom = Turtle("square")
    tom.penup()
    tom.goto(location)
    tom.color("white")
    return tom
# Game over title in the screen..
def game_over():
    tom = Turtle()
    tom.penup()
    tom.color("white")
    tom.write("Game_over",move=False,align="center",font=("Arial",12,"normal"))
    return False


# Snake head collosion with body.
def head_collosion(snake_length):
    for i in range(2,snake_length-1):
        if snake_head.distance(all_squares[i]) < 10:
            return game_over()

    return True


# Wall defined here....
def wall_range():
    x_coordinate = int(snake_head.xcor())
    y_coordinate = int(snake_head.ycor())
    if x_coordinate > 280 or x_coordinate < -280 or y_coordinate < -280 or y_coordinate > 280:
        return game_over()
    return True

# Scoreboard turtle../
def scoring():
    scoreboard.reset()
    global score
    score +=1
    scoreboard.penup()
    scoreboard.pencolor("white")
    scoreboard.hideturtle()
    scoreboard.goto(0,280)
    scoreboard.write(f"Score: {score}",move=False,align="center",font=("Arial",12,"normal"))

# other variables
coordinates = [(0,0),(-20,0),(-40,0)]
all_squares = []
is_on = True    # Game Start
snake_length = len(all_squares) # length of the snake
score = 0 # for couting score   
scoreboard = Turtle()
scoreboard.penup()
scoreboard.pencolor("white")
scoreboard.hideturtle()
scoreboard.goto(0,280)
scoreboard.write(f"Score: {score}",move=False,align="center",font=("Arial",12,"normal"))

# Starting food 
food = Turtle("circle")
food.penup()
food.goto(randint(-280,280),randint(-280,280))
food.color("blue")


# Snake body is being created here
for i in range(3):
    all_squares.append(snake(coordinates[i]))


# Snake head creating
snake_head = all_squares[0]




# Controlling keys...
screen.onkey(up,"Up")
screen.onkey(down,"Down")
screen.onkey(right,"Right")
screen.onkey(left,"Left")


# Snake motion, food and collosion.
while is_on:
    screen.update()
    time.sleep(0.1)
    
    # ScoreBoard at the top of the display..
    
    # Keep moving
    for i in range(len(all_squares)-1,0,-1):
        all_squares[i].goto(all_squares[i-1].position())
    snake_head.forward(20)
    is_on = head_collosion(snake_length)

    # food generator
    if snake_head.distance(food) < 20:
        snake_length = len(all_squares)
        scoring()
        food.reset()
        food.penup()
        food.goto(randint(-280,280),randint(-280,280))
        food.color("blue")
        all_squares.append(snake(all_squares[len(all_squares)-1].position()))
    is_on = wall_range()

screen.exitonclick()