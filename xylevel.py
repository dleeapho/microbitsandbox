# A two-axis bubble level that uses the BBC microbit's accelerometer
from microbit import display, accelerometer, sleep

circle = display.Image( "02220:"
                        "20002:"
                        "20002:"
                        "20002:"
                        "02220:")
display.show(circle)

while True:

    tgt_bright = 9
    bubble_bright = 6

    scale = 30
    max_x = 2
    max_y = max_x
    
    lx, ly, lz = accelerometer.get_values()
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
        dot_brightness = tgt_bright
    else:
        dot_brightness = bubble_bright

    dotx = max_x - lx
    doty = max_y - ly

    background = display.get_pixel(dotx, doty)
    display.set_pixel(dotx, doty, dot_brightness)
    if dot_brightness == tgt_bright:
        display.set_pixel(dotx + 1, doty, dot_brightness)
        display.set_pixel(dotx - 1, doty, dot_brightness)
        display.set_pixel(dotx, doty + 1, dot_brightness)
        display.set_pixel(dotx, doty - 1, dot_brightness)
        
    sleep(100)
    
    display.set_pixel(dotx, doty, background)   
    if dot_brightness == tgt_bright:
        display.set_pixel(dotx + 1, doty, 0)
        display.set_pixel(dotx - 1, doty, 0)
        display.set_pixel(dotx, doty + 1, 0)
        display.set_pixel(dotx, doty - 1, 0)
    
    