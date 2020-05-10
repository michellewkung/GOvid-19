from microbit import *
import time


people = 0
t_end = time.time() + 60 * 15

while time.time() < t_end: 
# read PIR motion sensor    
    reading = pin0.read_digital()
    sleep (10000)
    if reading == 1:
        people += 1;
    if button_a or button_b was_pressed and people =< 15:
        display.scroll("GO")
    elif button_a or button_b was_pressed and people => 15:
        display.scroll("STOP!")

        
        


    
    
