from turtle import Turtle, Screen
import os
import binascii
import random 

def random_hex_string(length=3):
    return binascii.b2a_hex(os.urandom(length)).decode()


timmy = Turtle()
timmy.shape("turtle")
timmy.pensize(10)
timmy.speed(0)
angles = [0,90,180,270]
for i in range(200):
    timmy.color(f"#{random_hex_string()}")
    timmy.forward(20)
    timmy.setheading(random.choice(angles))
    

Screen().mainloop()