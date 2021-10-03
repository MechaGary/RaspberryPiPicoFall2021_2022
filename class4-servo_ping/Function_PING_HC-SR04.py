# This code has the BeetleBot run FWD at top spped.
# If the LHS side whisker bumps an object, Beetbot backs up and makes a righthand turn to avoid it.
# The time BeetleBot backs up is random, from 1.5 seconds to 6 seconds,.
# It will stop backing up if an object is detected 7 inches from the
# HC-SR04 ping sensor in the reat of BeetleBot.
# If the RHS whisker encounters an object, the behavior is the same except Beetlebot turns left after backing up.


from machine import Pin
# Pin uses the GPIO value , not the actual pin number 
import utime
import random


AliveLED = Pin(25,machine.Pin.OUT)

AliveLED.value(1)

PingTrigger=Pin(9,Pin.OUT)  #GP9 is physical pin 12
PingEcho=Pin(8,Pin.IN)  #GP8 is physical pin 11
###  !!!!!! NOTE in Thonny the software will throw misleading errors if the hardware is not wired !!!!!

def Ping():
    echotries=0
    PingTrigger.low()
    utime.sleep_us(2)  # note sleep_us is for microsecs
    PingTrigger.high()
    utime.sleep_us(10)
    PingTrigger.low()
    while ((PingEcho.value() == 0) and (echotries<30)):
        EchoStartTime = utime.ticks_us()
        echotries=echotries+1
         # This check bails out of the loop on a problem with a long echo  or failed echo, I havent been able to prove its needed.
         
    while PingEcho.value()==1:
        EchoHeard = utime.ticks_us()
    PingDeltaTime=EchoHeard-EchoStartTime
    PingDistance_cm =(PingDeltaTime*.0343)/2  # sound is 343.2 m/s .0343 cm/usec
    PingDistance_in=(PingDistance_cm)/2.54
    #print ("Measured distance is ",PingDistance_cm, "cm"  )
    print ("Measured distance is ",PingDistance_in, "inches"  )
    #print ("Echotries =", echotries)
    return PingDistance_in

while True:  #this is start of the main loop routine
    PingDistance=Ping()
    utime.sleep(.2)
    if (PingDistance<3):
        AliveLED.low()
        utime.sleep(10)
    else: AliveLED.high()
     