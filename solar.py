# Completed Successfully
from turtle import *
import time
speed(0)
title("Solar System")
bgcolor("black")
color("white")
colormode(255)

penup()
goto(0, 200)
color("white")
write("Solar system", font=("times new roman", 40, "italic"), align="center")
pendown()


def round_do(gox, goy, rad):

    setheading(0)
    penup()
    goto(gox, goy)
    pendown()
    circle(rad)


def solar(colors, rad, gox, goy, name, move):
    hideturtle()
    penup()
    goto(gox, goy)
    pendown()
    color(colors)
    begin_fill()
    circle(rad)
    end_fill()
    penup()
    setheading(90)
    forward(move)
    pendown()
    write(name, font=("times new roman", 20, "italic"), align="center")


round_do(-400, -200, 220)
round_do(-400, -300, 320)
round_do(-400, -400, 420)
round_do(-400, -500, 520)
round_do(-400, -600, 620)
round_do(-400, -700, 720)
round_do(-400, -800, 820)
round_do(-400, -900, 920)

# sun
solar((253, 184, 19), 50, -390, -50, "Sun", 130)
# mercury
solar((205, 203, 202), 30, -150, 0, "Mercury", 30)
# venus
solar((139, 125, 130), 30, -50, 0, "Venus", 30)
# earth
solar((107, 147, 214), 30, 50, 0, "Earth", 30)
# mars
solar((246, 241, 213), 30, 150, 0, "Mars", 30)
# jupiter
solar((188, 175, 178), 30, 250, 0, "Jupiter", 30)
# saturn
solar((234, 214, 184), 30, 350, 0, "Saturn", 30)
# uranus
solar((209, 231, 231), 30, 450, 0, "Uranus", 30)
# neptune
solar((44, 78, 81), 30, 550, 0, "Neptune", 30)
time.sleep(2)
penup()
goto(100, -150)
pendown()
write("Thanks for watching!", font=("Times new roman", 50, "bold"), align="center")
time.sleep(2)
quit()
done()
