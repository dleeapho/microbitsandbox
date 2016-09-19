# A two-axis bubble level that uses the BBC microbit's accelerometer
from microbit import *

circle = Image( "02220:"
                "20002:"
                "20002:"
                "20002:"
                "02220:")
display.show(circle)

while True:

    scale = 30
    max_x = 2
    max_y = max_x
    
    (lx, ly, lz) = accelerometer.get_values()
    lx = int(lx / scale)
    ly = int(ly / scale)

    if lx < -max_x:
        lx = -max_x
    elif lx > max_x:
        lx = max_x
    
    if ly < -max_y:
        ly = -max_y
    elif ly > max_y:
        ly = max_y

    if lx == 0 and ly == 0:
        dotbrightness = 9
    else:
        dotbrightness = 7

    dotx = 2 - lx
    doty = 2 - ly

    background = display.get_pixel(dotx, doty)
    display.set_pixel(dotx, doty, dotbrightness)
    if dotbrightness == 9:
        display.set_pixel(dotx + 1, doty, dotbrightness)
        display.set_pixel(dotx - 1, doty, dotbrightness)
        display.set_pixel(dotx, doty + 1, dotbrightness)
        display.set_pixel(dotx, doty - 1, dotbrightness)
        
    sleep(100)
    
    display.set_pixel(dotx, doty, background)   
    if dotbrightness == 9:
        display.set_pixel(dotx + 1, doty, 0)
        display.set_pixel(dotx - 1, doty, 0)
        display.set_pixel(dotx, doty + 1, 0)
        display.set_pixel(dotx, doty - 1, 0)
    
    