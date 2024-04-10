from turtle import Turtle, Screen
import os
import binascii

def random_hex_string(length=3):
    return binascii.b2a_hex(os.urandom(length)).decode()


timmy = Turtle()
timmy.shape("turtle")

shapes = 3
for i in range(17):
    timmy.color(f"#{random_hex_string()}")
    turn = 360 / shapes
    for j in range(shapes):
        timmy.right(turn)
        timmy.forward(100)
    shapes +=1

Screen().mainloop()