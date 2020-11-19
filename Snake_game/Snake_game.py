import turtle
import time
import random
gamespeed = 0.08
segments = []
flag = 0

snake = turtle.Turtle()
snake.shape('square')
snake.direction = 'Up'


wn = turtle.Screen()
wn.setup(600, 600)
wn.title("test")
wn.bgcolor("gold")
wn.title("Snake Game")


border = turtle.Turtle()
border.hideturtle()
border.pensize(7)
border.penup()
border.goto(210,210)
border.pendown()
border.setheading(270)


for i in range(4):
    border.forward(420)
    border.right(90)

border.penup()
border.goto(0,-250)
border.write("Press Q to exit", align="center", font=("Courier", 24, "normal"))


    
def snake_move():
    snake.penup()
    x = snake.xcor()
    y = snake.ycor()
    if snake.direction  == 'Up':
        snake.goto(x,y+20)
    elif snake.direction == 'Down':
        snake.goto(x,y-20)
    elif snake.direction == 'Left':
        snake.goto(x-20,y)
    elif snake.direction == 'Right':
        snake.goto(x+20,y)

    time.sleep(gamespeed)


def go_up():
    if snake.direction != "Down":
        snake.direction = "Up"
 
def go_down():
    if snake.direction != "Up":
        snake.direction = "Down"
 
def go_right():
    if snake.direction != "Left":
        snake.direction = "Right"
 
def go_left():
    if snake.direction != "Right":
        snake.direction = "Left"

def exitapp():
    global flag
    flag = 1
    

wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_right, "Right")
wn.onkey(go_left, "Left")
wn.onkey(exitapp, 'q')

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.shapesize(0.50, 0.50)
food.goto(100, 55)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("dark blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
score =0
pen.write("Score: {}".format(score), align="center", font=("Courier", 30, "bold"))





        
while True:
    wn.update()
    snake_move()

    if flag == 1:
        turtle.bye()
        break
    
    if snake.distance(food) <15:
        xf = random.randint(-200, 200)
        yf = random.randint(-200, 200)
        food.goto(xf, yf)

        
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        score = score+10
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Courier", 30, "bold"))
        

    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments)> 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x, y)

    if snake.xcor() > 200 or snake.xcor() < -200 or snake.ycor() > 200 or snake.ycor() < -200:
        snake.color("red")
        time.sleep(1)
        snake.color("black")
        snake.goto(0, 0)
        snake.direction = "stop"
        score =0
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Courier", 30, "bold"))
        
        for segment in segments:
           segment.goto(1000, 1000)
           
        segments = []

    if len(segments)>2:
        for segment in range(1,len(segments),1):
            if segments[segment].distance(snake) < 20:
                snake.color("red")
                time.sleep(1)
                snake.color("black")
                snake.goto(0, 0)
                snake.direction = "stop"
                score =0
                pen.clear()
                pen.write("Score: {}".format(score), align="center", font=("Courier", 30, "bold"))

             

                for segment in segments:
                   segment.goto(1000, 1000)
                segments=[]
                break















