from machine import Pin, ADC, PWM
import utime
PWM1A=PWM(Pin(2)) # GP2  pin 4 
PWM1A.freq(1000)


PotWiperCounts=ADC(Pin(26)) # can also call machine.ADC(3) 
#GP2OFFSET=288  # The PotWiperCounts when the pot is full CCW
#GP2GAIN=1.004 # GP2 read 65535 at full cw, however once 288 counts are
# subtracted from it, it needs multiplied by the ratio to make it back to 65535 full scale

while True:
    print(PotWiperCounts.read_u16())
#    PotWiperCountsReal=PotWiperCounts*1.0
#    PotWiperCountsReal=(PotWiperCountsReal-(GP2OFFSET))
# yes, in code you can read a value, do math, and put the value back to the same name
#    PotWiperCountsReal=1.004*PotWiperCounts
    duty=PotWiperCounts.read_u16()
    PWM1A.duty_u16(duty)
    utime.sleep(.05)
#    print("Adjusted GP2 value is:", PotWiperCountsReal)
    
# MAKE a NOTE what the PotWiperCounts are at full CW - full up________
# MAKE a NOTE what the PotWiperCounts are at full CCW - full down________
# The value at full CCW should be zero. The value it really shows is called OFFSET !!
# The next program you will correct the OFFSET and then also the gain error - The value at full CW !