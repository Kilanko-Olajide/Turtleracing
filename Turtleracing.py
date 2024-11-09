import turtle
import time
import random
WIDTH = 500
HEIGHT = 500

COLORS = ["red", "green", "blue", "orange", "yellow", "black", "purple", "pink", "brown", "cyan"]
random.shuffle(COLORS)
def turtle_init():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle racing!")

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 40)
        racer.pendown()
        turtles.append(racer)
    return turtles




def get_number_of_racers():
    while True:
        racers = input("How many racers do you want(2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print(f"{racers} is not valid.")
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print(f"{racers} is out of range.")

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randint(1, 20)
            
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT/2 - 20:
                return colors[turtles.index(racer)]


racers = get_number_of_racers()
turtle_init()
racers = int(racers)
colors = COLORS[:racers]
numberone = race(colors)
print(f"The winner of this turtle race is turtle {numberone}.")


time.sleep(10)
