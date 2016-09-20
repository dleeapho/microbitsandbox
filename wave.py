from microbit import *

def send_wave(direction, speed):
    lines = ["90000", "09000", "00900", "00090", "00009"]
    waves = [
        Image (lines[0]+":"+
               lines[0]+":"+
               lines[0]+":"+
               lines[0]+":"+
               lines[0]),
        Image (lines[1]+":"+
               lines[1]+":"+
               lines[1]+":"+
               lines[1]+":"+
               lines[1]),
        Image (lines[2]+":"+
               lines[2]+":"+
               lines[2]+":"+
               lines[2]+":"+
               lines[2]),
        Image (lines[3]+":"+
               lines[3]+":"+
               lines[3]+":"+
               lines[3]+":"+
               lines[3]),
        Image (lines[4]+":"+
               lines[4]+":"+
               lines[4]+":"+
               lines[4]+":"+
               lines[4])
    ]
    
    if direction:
        waves.reverse()

    display.show(waves, loop=False, delay=speed)
    return

to_left = True
while True:
    to_left = not to_left
    send_wave(to_left, 500)
