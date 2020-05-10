from microbit import *
import utime 
import machine

#let PIR motion sensor calibrate
sleep(10000)
people = 0
button = button_a or button_b


while True: 
    #display.show(running_time()/1000)
    if running_time()<60000 * 15:
# read PIR motion sensor    
        reading = pin0.read_digital();
        sleep (10);
        if reading == 1:
            people += 1;
        if button.was_pressed() and people <= 15:
            display.scroll("GO");
        elif button.was_pressed() and people >= 15:
            display.scroll("STOP!");
    else:
        machine.reset();
        
