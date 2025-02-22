import turtle
import time 
import random

delay = 0.1 

# Scores
score_1 = 0
score_2 = 0
high_score_1 = 0
high_score_2 = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by Ali Öztürk")
wn.bgcolor("green")
wn.setup(width= 1000, height= 720)
wn.tracer(0) # Turns off the screen updates

#Snake heads
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("purple")
head.penup()
head.goto(-180,0)
head.direction = "stop"

head_2 = turtle.Turtle()
head_2.speed(0)
head_2.shape("square")
head_2.color("dark blue")
head_2.penup()
head_2.goto(180,0)
head_2.direction = "stop"

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []
segments2 = []
# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(-200, 320)
pen.write("Score: 0 | High Score: 0", align= "center", font=("Courier", 14, "normal"))

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.shape("square")
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(200, 320)
pen2.write("Score: 0 | High Score: 0", align= "center", font=("Courier", 14, "normal"))

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
    
def go_up2():
    if head_2.direction != "down":
        head_2.direction = "up"

def go_down2():
    if head_2.direction != "up":
        head_2.direction = "down"

def go_left2():
    if head_2.direction != "right":
        head_2.direction = "left"

def go_right2():
    if head_2.direction != "left":
        head_2.direction = "right"

def move2():
    if head_2.direction == "up":
        y = head_2.ycor()
        head_2.sety(y + 20)
    if head_2.direction == "down":
        y = head_2.ycor()
        head_2.sety(y - 20)
    if head_2.direction == "left":
        x = head_2.xcor()
        head_2.setx(x - 20)
    if head_2.direction == "right":
        x = head_2.xcor()
        head_2.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

wn.onkeypress(go_up2, "Up")
wn.onkeypress(go_down2, "Down")
wn.onkeypress(go_left2, "Left")
wn.onkeypress(go_right2, "Right")

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

    wn.update()
   # Check for a collision with the border
    if head_2.xcor()>500:
        ycr = head_2.ycor()
        head_2.goto(-500, ycr)   
    elif head_2.xcor()<-500:
        ycr = head_2.ycor()
        head_2.goto(500, ycr)
    elif head_2.ycor()>360:
        xcr = head_2.xcor()
        head_2.goto(xcr,-360)
    elif head_2.ycor()<-360:
        xcr = head_2.xcor()
        head_2.goto(xcr,360)

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
        new_segment.color("pink")
        new_segment.penup()
        segments.append(new_segment)   
        # Increase the score
        score_1 += 10
        if score_1 > high_score_1:
            high_score_1 = score_1 
        pen.clear()
        pen.write(f"Score: {score_1} | High Score: {high_score_1}".format(score_1, high_score_1), align= "center", font=("Courier", 14, "normal"))

     
    if head_2.distance(food)< 20:
        # Move the food to random spot
        x = random.randrange(-480, 480, 20)
        y = random.randrange(-340, 340, 20)
        food.goto(x, y)
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("pink")
        new_segment.penup()
        segments2.append(new_segment)  
        # Increase the score
        score_2 += 10
        if score_2 > high_score_2:
            high_score_2 = score_2 
        pen2.clear()
        pen2.write(f"Score: {score_2}  High Score: {high_score_2}".format(score_2, high_score_2), align= "center", font=("Courier", 14, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    for index in range(len(segments2)-1, 0, -1):
        x = segments2[index-1].xcor()
        y = segments2[index-1].ycor()
        segments2[index].goto(x, y)
    # Move segment 0 to where the head is
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    if len(segments2)>0:
        x = head_2.xcor()
        y = head_2.ycor()
        segments2[0].goto(x, y)                  

    move()
    move2()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20: 
            time.sleep(1)
            head.goto(-180,0)
            head.direction = "stop"
              # Hide the segments 
            for segment in segments:
                segment.goto(1400, 1400)
            # Clear the segments lists
            segments.clear() 
            # Reset the delay 
            delay = 0.1
            # Resest the score
            score_1 = 0
            pen.clear()
            pen.write(f"Score: {score_1} | High Score: {high_score_1}".format(score_1, high_score_1), align="center", font=("Courier", 14, "normal"))

    for segment in segments:
        if segment.distance(head_2) < 20: 
            time.sleep(1)
            head_2.goto(180,0)
            head_2.direction = "stop"
              # Hide the segments 
            for segment in segments2:
                segment.goto(1400, 1400)
            # Clear the segments lists
            segments2.clear() 
            # Reset the delay 
            delay = 0.1
            # Resest the score
            score_2 = 0
            pen2.clear()
            pen2.write(f"Score: {score_2} | High Score: {high_score_2}".format(score_2, high_score_2), align="center", font=("Courier", 14, "normal"))

    for segment2 in segments2:
        if segment2.distance(head_2) < 20: 
            time.sleep(1)
            head_2.goto(180,0)
            head_2.direction = "stop"
              # Hide the segments 
            for segment2 in segments2:
                segment2.goto(1400, 1400)
            # Clear the segments lists
            segments2.clear() 
            # Reset the delay 
            delay = 0.1
            # Resest the score
            score_2 = 0
            pen2.clear()
            pen2.write(f"Score: {score_2} | High Score: {high_score_2}".format(score_2, high_score_2), align="center", font=("Courier", 14, "normal"))

    for segment2 in segments2:
        if segment2.distance(head) < 20: 
            time.sleep(1)
            head.goto(-180,0)
            head.direction = "stop"
              # Hide the segments 
            for segment in segments:
                segment.goto(1400, 1400)
            # Clear the segments lists
            segments.clear() 
            # Reset the delay 
            delay = 0.1
            # Resest the score
            score_1 = 0
            pen.clear()
            pen.write(f"Score: {score_1} | High Score: {high_score_1}".format(score_1, high_score_1), align="center", font=("Courier", 14, "normal"))

    if head.distance(head_2)<20:
        time.sleep(1)
        head.goto(-180,0)
        head.direction = "stop"
        # Hide the segments 
        for segment in segments:
            segment.goto(1400, 1400)
        # Clear the segments lists
        segments.clear() 
        # Resest the score
        score_1 = 0
        pen.clear()
        pen.write(f"Score: {score_1} | High Score: {high_score_1}".format(score_1, high_score_1), align="center", font=("Courier", 14, "normal"))
        head_2.goto(180,0)
        head_2.direction = "stop"      
        # Hide the segments 
        for segment2 in segments2:
            segment2.goto(1400, 1400)
        # Clear the segments lists
        segments2.clear() 
        # Resest the score
        score_2 = 0
        pen2.clear()
        pen2.write(f"Score: {score_2} | High Score: {high_score_2}".format(score_2, high_score_2), align="center", font=("Courier", 14, "normal"))

    time.sleep(delay)

wn.mainloop()  
