# Go-Stop
A people counter that helps users social distance

In order to make this counter you need to set up connect a Microbit to a PIR motion sensor. 
All code for this installation is written in MicroPython.

Instructions:
Connect the PIR motion sensor to the microbit. Position it at the side of an entryway, about 1 metre of the ground, facing the opposite side of the entryway. After the physical installation push the code go-stop.py onto the Microbit. Leave it for 5 minutes, afterwards the PIR motion sensor will detect when objects move in front of it. Every time the sensor detects a movement, it will add 1 to the count. It will run for 15 minutes, and then restart. 

When a user pushes either button a or b, the display will tell the user if it is safe to go by scrolling "Go" or if it is unsafe by scrolling "Stop". The device determines that it is unsafe if the count is above 15, and that it is safe if the count is under 15. 
