# Simple pong
from microbit import *
import random

player = [button_a, button_b]
server = 0
receiver = 1
court = [0, 1, 2, 3, 4]
baseline = 3

def serve(from_x, from_y):
    "serves a ball and returns True to indicate the game is now in play and resets the speed of the game"
    serving_speed = 10000
    is_inplay = True
    for setserve in range(0,3):
        sleep(150)
        display.set_pixel(ballx, bally, 9)
        sleep(150)
        display.set_pixel(ballx, bally, ballbright)
    return is_inplay, serving_speed

def evaluate_turn(is_returned, position, current_speed, return_speed):
    "evaluates whether the rally is still in play and if so the new pace of the game "
    is_inplay = True
    speedup_factor = 3  # smaller means returns speed up more quickly
    if is_returned:
        if position == baseline:
            current_speed = current_speed - (return_speed // speedup_factor)
        else:
            is_inplay = False       
            if position < baseline:
                display.scroll("Fault")
            if position > baseline:
                display.scroll("Miss")
    else:
        display.scroll("Ace")
        is_inplay = False
    return is_inplay, current_speed

def wait_for_hit(receivingplayer, speed):
    "waits and indicates if the play has pressed a button and how long he/she waited"
    returned = False
    for tick in range(0, speed):
        if receivingplayer.was_pressed():
            returned = True
            break
    return returned, tick

is_inplay = False
while True:
    # the rally loop
    bally = random.randint(0,4)
    returned = False

    for ballx in court:
        # the ball moving loop
        position = court.index(ballx)
        ballbright = position + 5
        if not is_inplay:
            is_inplay, rally_speed = serve(ballx, bally)
        display.set_pixel(ballx, bally, ballbright)
        returned, return_force = wait_for_hit(player[receiver], rally_speed)
        display.set_pixel(ballx, bally, 0)  
        if returned:
            break 
    is_inplay, rally_speed = evaluate_turn(returned, position, rally_speed, return_force)
    #clear the button buffer
    button_a.was_pressed()
    button_b.was_pressed()

    player.reverse()
    court.reverse()
        