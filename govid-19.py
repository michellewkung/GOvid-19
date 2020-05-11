from microbit import *
import utime 
import machine

#let PIR motion sensor sensitize
sleep(10000)
people = 0

#Main loop
while True: 
    #display.show(running_time()/1000)
    if running_time() < 60000 * 15:
        if pin0.read_digital():
            people += 1;
    if button_a.was_pressed() and people <= 15:
        display.scroll("GO");
    elif button_a.was_pressed() and people >= 15:
        display.scroll("STOP!");
    elif button_b.was_pressed() and people <= 15:
        display.scroll("GO");
    elif button_b.was_pressed() and people >= 15:
         display.scroll("STOP!");
    else:
        machine.reset();
