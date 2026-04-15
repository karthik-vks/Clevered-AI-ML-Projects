import math
import turtle
import random

screen = turtle.Screen()
screen.setup(600, 600)
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)
t.penup()

treasure_x = random.randint(-100, 100)
treasure_y = random.randint(-100, 100)

prev_dist = None

def check_distance():
    global prev_dist
    curr_dist = math.sqrt((t.xcor() - treasure_x)**2 + (t.ycor() - treasure_y)**2)
    
    if t.distance(treasure_x, treasure_y) < 5:
        t.color("red")
        t.write("YOU FOUND IT!", align="center", font=("Arial", 20, "bold"))
        print(f"Treasure was at: {treasure_x}, {treasure_y}")
        screen.onkey(None, "Up")
        screen.onkey(None, "Down")
        screen.onkey(None, "Left")
        screen.onkey(None, "Right")
        return

    if prev_dist is not None:
        if curr_dist < prev_dist:
            t.color("orange") # Warmer
        else:
            t.color("blue")   # Colder
            
    prev_dist = curr_dist

def move_up():
    t.setheading(90)
    t.forward(10)
    check_distance()

def move_down():
    t.setheading(270)
    t.forward(10)
    check_distance()

def move_left():
    t.setheading(180)
    t.forward(10)
    check_distance()

def move_right():
    t.setheading(0)
    t.forward(10)
    check_distance()

screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

print("Use the Arrow Keys to find the treasure!")
print("Orange = Warmer | Blue = Colder")

screen.mainloop()
