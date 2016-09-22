# Simple pong
from microbit import *
import random

turn = [button_a, button_b]
server = 0
receiver = 1
court = [0, 1, 2, 3, 4]

serving_speed = 10000
speed = serving_speed
speedup_factor = 3  # the lower means returns speed up more
ballbright = 9


serving = True
while True:
    # the rally loop
    bally = random.randint(0,4)
    returned = False
    returntick = 0
    for ballx in court:
        # the ball moving loop
        position = court.index(ballx)
        ballbright = position + 5
        display.set_pixel(ballx, bally, ballbright)
        if serving:
            serving = False
            speed = serving_speed
            for setserve in range(0,3):
                sleep(150)
                display.set_pixel(ballx, bally, 9)
                sleep(150)
                display.set_pixel(ballx, bally, ballbright)
        for tick in range(0, speed):
            if turn[receiver].was_pressed():
                returned = True
                returntick = tick
                break
        display.set_pixel(ballx, bally, 0)  
        if returned:
            break 
    if returned:
        if position == 3:
            speed = speed - (tick // speedup_factor)
        else:
            serving = True       
            if position < 3:
                display.scroll("Fault")
            if position > 3:
                display.scroll("Miss")
    else:
        display.scroll("Ace")
        serving = True

    turn.reverse()
    court.reverse()
        