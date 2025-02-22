import turtle
import time 
import random

delay = 0.1 

# Score 
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by Ali Öztürk")
wn.bgcolor("light green")
wn.setup(width= 1000, height= 720)
wn.tracer(0) # Turns off the screen updates

#Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake Foods
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("dark red")
food.penup()
food.goto(0,100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 320)
pen.write("Score: 0  High Score: 0", align= "center", font=("Courier", 24, "normal"))

# Functions

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor()>500:
        ycr = head.ycor()
        head.goto(-500, ycr)   
    elif head.xcor()<-500:
        ycr = head.ycor()
        head.goto(500, ycr)
    elif head.ycor()>360:
        xcr = head.xcor()
        head.goto(xcr,-360)
    elif head.ycor()<-360:
        xcr = head.xcor()
        head.goto(xcr,360) 

    # Check for a collision with the food
    if head.distance(food)< 20:
        # Move the food to random spot
        x = random.randrange(-480, 480, 20)
        y = random.randrange(-340, 340, 20)
        food.goto(x, y)
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        # Shorten the delay
        delay -= 0.001   
        # Increase the score
        score += 10
        if score > high_score:
            high_score = score 
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}".format(score, high_score), align= "center", font=("Courier", 24, "normal"))
        
    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    # Move segment 0 to where the head is
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20: 
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
              # Hide the segments 
            for segment in segments:
                segment.goto(1400, 1400)
            # Clear the segments lists
            segments.clear() 
            # Reset the delay 
            delay = 0.1
            # Resest the score
            score = 0
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()   