# Simple pong
from microbit import *
import random

turn = [button_a, button_b]
server = 0
receiver = 1
court = [0, 1, 2, 3, 4]
speed = 10000

ballbright = 9
ballserve = 4
service = True
while True:
    bally = random.randint(0,4)
    returned = False
    returntick = 0
    for ballx in court:
        display.set_pixel(ballx, bally, ballbright)
        position = court.index(ballx)
        if service:
            service = False
            for setserve in range(0,3):
                sleep(200)
                display.set_pixel(ballx, bally, ballserve)
                sleep(200)
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
        if position < 3:
            display.scroll("Fault")
            service = True            
        if position > 3:
            display.scroll("Miss")
            service = True
    else:
        display.scroll("Aced")
        service = True
    turn.reverse()
    court.reverse()
        