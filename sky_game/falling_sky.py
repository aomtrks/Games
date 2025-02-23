import turtle
import time
import random
import pygame

pygame.init()

def sound():
   a = pygame.mixer.Sound("C:/Users/Muhammed Ali/Documents/GAMES/sky_game/yeap.mp3")
   a.play()

def sound2():
   a = pygame.mixer.Sound("C:/Users/Muhammed Ali/Documents/GAMES/sky_game/aww.mp3")
   a.play()
def final_sound():
    a = pygame.mixer.Sound("C:/Users/Muhammed Ali/Documents/GAMES/sky_game/final_sound.mp3")
    a.play()
score = 0 
lives = 10

wn = turtle.Screen()
wn.title("FALLING SKIES by Ali Ozturk")
wn.bgcolor("white")
wn.setup(width=800, height=600)
wn.tracer(0)   

#Register shapes
turtle.register_shape("C:/Users/Muhammed Ali/Documents/GAMES/sky_game/dogr.gif")
turtle.register_shape("C:/Users/Muhammed Ali/Documents/GAMES/sky_game/dog.gif")
turtle.register_shape("C:/Users/Muhammed Ali/Documents/GAMES/sky_game/ekmek.gif")
turtle.register_shape("C:/Users/Muhammed Ali/Documents/GAMES/sky_game/dog2.gif")


delay= 0.01
# Add the player
player = turtle.Turtle()
player.speed(0)
player.shape("C:/Users/Muhammed Ali/Documents/GAMES/sky_game/dogr.gif")
player.color("black")
player.penup()
player.goto(0,-250)
player.direction = "stop"

# Create a list of good_guys
good_guys = []

# Add the good_guys
for _ in range(20):
    good_guy = turtle.Turtle()
    good_guy.speed(0)
    good_guy.shape("C:/Users/Muhammed Ali/Documents/GAMES/sky_game/ekmek.gif")
    good_guy.color("gold")
    good_guy.penup()
    good_guy.goto(100,250)
    good_guy.speed= random.randint(1, 4)
    good_guys.append(good_guy)

# Create a list of bad_guys
bad_guys = []

# Add the bad_guys
for _ in range(20):
    bad_guy = turtle.Turtle()
    bad_guy.speed(0)
    bad_guy.shape("C:/Users/Muhammed Ali/Documents/GAMES/sky_game/dog2.gif")
    bad_guy.color("red")
    bad_guy.penup()
    bad_guy.goto(-100,250)
    bad_guy.speed= random.randint(1, 4)
    bad_guys.append(bad_guy)

# Make a pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.goto(0, 260)
font = ("courier",24, "normal")
pen.write(f"Score: {score}  Lives: {lives}", align="center", font= font)

# Functions

def go_up():
    player.direction = "up"

def go_down():
    player.direction = "down"

def go_left():
    player.direction = "left"

def go_right():
    player.direction = "right"

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")



# Main game loop
while True:
    # Update screen
    wn.update()
    if lives<1:
        final_sound()
        pen.clear()
        pen.goto(0,0)
        pen.color("red")
        pen.showturtle()
        wn.bgcolor("dark blue")
        pen.write(f"YOU DİED GAME OVER Score: {score}", align="center", font=("courier",30, "normal"))
        time.sleep(1)
        break
    # Move the player
    if player.direction =="up" and player.ycor()<280:
        y = player.ycor()
        y+=3
        player.sety(y)
    
    if player.direction =="down"and player.ycor()>-280:
        y = player.ycor()
        y-=3
        player.sety(y)
         
    if player.direction =="left"and player.xcor()>-390:
        x = player.xcor()
        x-=3
        player.setx(x)
        player.shape("C:/Users/Muhammed Ali/Documents/GAMES/sky_game/dog.gif")

    if player.direction =="right"and player.xcor()<380:
        x = player.xcor()
        x+=3
        player.setx(x)
        player.shape("C:/Users/Muhammed Ali/Documents/GAMES/sky_game/dogr.gif")

    # Move the good guy
    for good_guy in good_guys:
        y = good_guy.ycor()
        y -= good_guy.speed
        good_guy.sety(y)
        if y < -300:
            x = random.randrange(400, -420, -20)
            y = random.randrange(200, 300, 20)
            good_guy.goto(x, y)
        # Check for a collision with the player
        if good_guy.distance(player)< 20:
            sound()
            x = random.randrange(400, -420, -20)
            y = random.randrange(200, 300, 20)
            good_guy.goto(x, y)
            score += 10
            pen.clear()
            pen.write(f"Score: {score}  Lives: {lives}", align="center", font= font)
            time.sleep(delay)
    # Move the bad guy
    for bad_guy in bad_guys:
        y = bad_guy.ycor()
        y -= bad_guy.speed
        bad_guy.sety(y)
        if y < -300:
            x = random.randrange(400, -420, -20)
            y = random.randrange(200, 300, 20)
            bad_guy.goto(x, y)
        # Check for a collision with the player
        if bad_guy.distance(player)< 20:
            sound2()
            x = random.randrange(400, -420, -20)
            y = random.randrange(200, 300, 20)
            bad_guy.goto(x, y)
            lives -= 1 
            pen.clear()
            pen.write(f"Score: {score}  Lives: {lives}", align="center", font= font)


    time.sleep(delay)

wn.mainloop()


