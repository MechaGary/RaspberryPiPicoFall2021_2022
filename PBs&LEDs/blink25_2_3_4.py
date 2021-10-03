from machine import Pin
import utime
led_GP25= Pin(25, Pin.OUT) #remember this pinout is not accessible, the LED is hardwired on the Pico.
led_GP2 = Pin(2, Pin.OUT) # GP2 is physical pin 4
led_GP3 = Pin(3, Pin.OUT) # GP3 is physical pin 5
led_GP4 = Pin(4, Pin.OUT) # GP3 is physical pin 6
led_GP25.low() # this line ensures the LED is initilized to the OFF state.
#Initialzing outputs and values are very important to start a machine in a safe predictable way.
led_GP2.low()
led_GP3.low()
led_GP4.low()
while True:
    led_GP25.toggle()
    utime.sleep(.1)
    led_GP2.toggle()
    utime.sleep(.1)
    led_GP3.toggle()
    utime.sleep(.1)
    led_GP4.toggle()
    utime.sleep(.1)