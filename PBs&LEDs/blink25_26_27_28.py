from machine import Pin
import utime
led_GP25= Pin(25, Pin.OUT) #remember this pinout is not accessible, the LED is hardwired on the Pico.
led_GP26 = Pin(26, Pin.OUT)
led_GP27 = Pin(27, Pin.OUT)
led_GP28 = Pin(28, Pin.OUT)
led_GP25.low() # this line ensures the LED is initilized to the OFF state.
#Initialzing outputs and values are very important to start a machine in a safe predictable way.
while True:
    led_GP25.toggle()
    utime.sleep(.1)
    led_GP26.toggle()
    utime.sleep(.1)
    led_GP27.toggle()
    utime.sleep(.1)
    led_GP28.toggle()
    utime.sleep(.1)