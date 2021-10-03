from machine import Pin
import utime
pushbutton1= Pin(16, machine.Pin.IN,machine.Pin.PULL_DOWN)#GP16 is pin 21
# the open contacts of switch and pushbutton dont provide voltage to the Pico input
# it jumps around called floating.
# the pull down feature turns on a resistor between the input and GND so the input reads 0 (low) when not pushed
# the pull up feature turns on a resistor between the input and 3V so the input reads 1 (HIGH) when not pushed
pushbutton2= Pin(17, machine.Pin.IN,machine.Pin.PULL_DOWN)#GP17 is pin22

pushbutton1LED= Pin(25, machine.Pin.OUT)#GP25 is the Pico mounted LED
pushbutton2LED= Pin(2, machine.Pin.OUT)#GP2 is Pico pin 4
pushbutton2Buzzer= Pin(14, machine.Pin.OUT)#GP14 is Pico pin19

while True:
    if pushbutton1.value() ==1:
        pushbutton1LED.value(1)
    if pushbutton1.value() ==0:
        pushbutton1LED.value(0)
# this is a brute force way to code both states of the pushbutton. Another way is using the if....else statement
    if pushbutton2.value() ==1:
        pushbutton2LED.value(1)
    if pushbutton2.value() ==0:
        pushbutton2LED.value(0)
# added in buzzer output
    if pushbutton2.value() ==1:
        pushbutton2Buzzer.value(1)
    if pushbutton2.value() ==0:
        pushbutton2Buzzer.value(0)
        
    utime.sleep(.1) # this is to help debounce the pushbutton