import turtle
import math 
import random
import time

delay = 0.1
lives = 10

# Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("CAVE GAME by Ali Ozturk")
wn.setup(700, 700)
wn.tracer(0)

#Register shapes
turtle.register_shape("C:/Users/Muhammed Ali/Documents/GAMES/maze_game/wizard_right.gif.gif")
turtle.register_shape("C:/Users/Muhammed Ali/Documents/GAMES/maze_game/wizard_left.gif.gif")
turtle.register_shape("C:/Users/Muhammed Ali/Documents/GAMES/maze_game/treasure.gif")

# Create Pen 
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("C:/Users/Muhammed Ali/Documents/GAMES/maze_game/wizard_right.gif.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0
    
    def go_up(self):
        #Calculate the spot to move to
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24
        #Check if the space has a wall
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        #Calculate the spot to move to
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24
        #Check if the space has a wall
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            
    def go_left(self):
        #Calculate the spot to move to
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()

        self.shape("C:/Users/Muhammed Ali/Documents/GAMES/maze_game/wizard_left.gif.gif")

        #Check if the space has a wall
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            
    def go_right(self):
        #Calculate the spot to move to
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor() 

        self.shape("C:/Users/Muhammed Ali/Documents/GAMES/maze_game/wizard_right.gif.gif")

        #Check if the space has a wall
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a**2) + (b**2))
        if distance < 20:
            return True
        else:
            return False

class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C:/Users/Muhammed Ali/Documents/GAMES/maze_game/treasure.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

class Enemy(turtle.Turtle):
    def __init__(self, x, y, direction):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.direction = direction

    def go_up1(self):
        #Calculate the spot to move to
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24
        #Check if the space has a wall
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            direction = random.choice(["down", "left", "right"])
            self.direction = direction
            self.move_enemy(direction)

    def go_down1(self):
        #Calculate the spot to move to
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24
        #Check if the space has a wall
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            direction = random.choice(["up", "left", "right"])
            self.direction = direction
            self.move_enemy(direction)
    def go_left1(self):
        #Calculate the spot to move to
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()
        #Check if the space has a wall
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            direction = random.choice(["up", "down", "right"])
            self.direction = direction
            self.move_enemy(direction)
    def go_right1(self):
        #Calculate the spot to move to
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor() 
        #Check if the space has a wall
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            direction = random.choice(["up", "down", "left"])
            self.direction = direction
            self.move_enemy(direction)

    def stop(self):
        self.goto(self.xcor(), self.ycor())
    
    def move_enemy(self, direction):
        if direction == "up":
            self.go_up1()
        elif direction =="down":
            self.go_down1()
        elif direction =="left":
            self.go_left1()
        elif direction =="right":
            self.go_right1()
        else:
            self.stop()


# Create levels list
levels = [""]

# Define first level
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP XXXXXXXE         XXXXX",
"X  XXXXXXX  XXXXXX  XXXXX",
"X       XX  XXXXXX  XXXXX",
"X       XX  XXX       XXX",
"XXXXXX  XX  XXX       XXX",
"XXXXXX  XX  XXXXXX  XXXXX",
"XXXXXX  XX    XXXX  XXXXX",
"X  XXXE       XXXXT XXXXX",
"X  XXX  XXXXXXXXXXXXXXXXX",
"X         XXXXXXXXXXXXXXX",
"X                XXXXXXXX",
"XXXXXXXXXXXX     XXXXX  X",
"XX      XXXXXXX  XXXXX  X",
"XX      XXXXXXXE        X",
"XX                      X",
"XX        XXXXXXXXXXXXXXX",
"XXXXX     XXXX         XX",
"XXXXX     XXXX         XX",
"XXXXX             XXXXXXX",
"XXXXX             XXXXXXX",
"XXXXXXXXXX    E   XXXXXXX",
"X             XXXXXXXXXXX",
"X T           XXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]
#Add a treasures list
treasures = []

#Add enemy list
enemies = []

# Add level to levels list
levels.append(level_1)

# Create level setup function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level)):
            #Get character at each x,y coordinate
            #NOTE the order of y and x in the next line
            character = level[y][x]
            #Calculate the screen x,y coordinates
            screen_x = - 288 + (x * 24)
            screen_y = 288 - (y * 24)
            
            #Check if it is an X (representing a wall)
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))

            #Check if it is a P (representing the player)
            if character == "P":
                player.goto(screen_x, screen_y)

            #Check if it is a T (representing Treasure)
            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))
            #Check if it is a E (representing Enemy)
            if character =="E":
                enemy = Enemy(screen_x, screen_y, "stop")
                enemies.append(enemy)

# Create class instances
pen = Pen()
player = Player()

#Create wall coordinate
walls = []

# Set up the level
setup_maze(levels[1])

#Keyboard Binding
turtle.listen()
turtle.onkeypress(player.go_up, "w")
turtle.onkeypress(player.go_down, "s")
turtle.onkeypress(player.go_left, "a")
turtle.onkeypress(player.go_right, "d")

#Turn off screen updates
wn.tracer(0)

for enemy in enemies:
    direction = random.choice(["up", "down", "left", "right"])
    enemy.direction = direction
# Main game loop
while True:
    #Update screen
    wn.update()
    #Check for player collision with treasure 
    #Iterate throuh terasure list
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            print(f"Player gold: {player.gold}")
            treasure.destroy()
            treasures.remove(treasure)
    for enemy in enemies:
        enemy.move_enemy(direction)
        if player.is_collision(enemy):
            lives -=1
    
    time.sleep(delay)

wn.mainloop()

#https://cloudconvert.com/png-to-gif
#https://online-audio-converter.com/tr/
